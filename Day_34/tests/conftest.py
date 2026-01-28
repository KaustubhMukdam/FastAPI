import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from src.database.core import Base, get_db
from src.main import app
from src.entities.user import User
from src.entities.todo import Todo
from src.auth.service import get_password_hash
from uuid import uuid4

# Use an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="function")
def test_db():
    """Create a fresh database for each test"""
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create a session
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        # Drop all tables after the test
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with overridden database dependency"""
    def override_get_db():
        try:
            yield test_db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()

@pytest.fixture
def test_user(test_db):
    """Create a test user in the database"""
    user = User(
        id=uuid4(),
        email="test@example.com",
        first_name="Test",
        last_name="User",
        password_hash=get_password_hash("testpassword123")
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    return user

@pytest.fixture
def test_user_2(test_db):
    """Create a second test user in the database"""
    user = User(
        id=uuid4(),
        email="test2@example.com",
        first_name="Test2",
        last_name="User2",
        password_hash=get_password_hash("testpassword456")
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    return user

@pytest.fixture
def auth_token(client, test_user):
    """Get an authentication token for the test user"""
    response = client.post(
        "/auth/token",
        data={
            "username": "test@example.com",
            "password": "testpassword123"
        }
    )
    assert response.status_code == 200
    return response.json()["access_token"]

@pytest.fixture
def auth_headers(auth_token):
    """Get authorization headers with the test user's token"""
    return {"Authorization": f"Bearer {auth_token}"}

@pytest.fixture
def test_todo(test_db, test_user):
    """Create a test todo in the database"""
    todo = Todo(
        id=uuid4(),
        user_id=test_user.id,
        description="Test Todo",
        is_completed=False
    )
    test_db.add(todo)
    test_db.commit()
    test_db.refresh(todo)
    return todo