import pytest
from uuid import uuid4
from datetime import timedelta
from src.auth import service, model
from src.entities.user import User
from src.exceptions import AuthenticationError


class TestPasswordHashing:
    """Test password hashing and verification"""
    
    def test_get_password_hash(self):
        """Test that password hashing returns a hash"""
        password = "testpassword123"
        hashed = service.get_password_hash(password)
        
        assert hashed is not None
        assert hashed != password
        assert len(hashed) > 0
    
    def test_verify_password_correct(self):
        """Test that correct password verification works"""
        password = "testpassword123"
        hashed = service.get_password_hash(password)
        
        assert service.verify_password(password, hashed) is True
    
    def test_verify_password_incorrect(self):
        """Test that incorrect password verification fails"""
        password = "testpassword123"
        wrong_password = "wrongpassword"
        hashed = service.get_password_hash(password)
        
        assert service.verify_password(wrong_password, hashed) is False


class TestUserAuthentication:
    """Test user authentication"""
    
    def test_authenticate_user_success(self, test_db, test_user):
        """Test successful user authentication"""
        user = service.authenticate_user(
            test_db,
            "test@example.com",
            "testpassword123"
        )
        
        assert user is not False
        assert isinstance(user, User)
        assert user.email == "test@example.com"
    
    def test_authenticate_user_wrong_password(self, test_db, test_user):
        """Test authentication fails with wrong password"""
        user = service.authenticate_user(
            test_db,
            "test@example.com",
            "wrongpassword"
        )
        
        assert user is False
    
    def test_authenticate_user_nonexistent_email(self, test_db):
        """Test authentication fails with non-existent email"""
        user = service.authenticate_user(
            test_db,
            "nonexistent@example.com",
            "anypassword"
        )
        
        assert user is False


class TestTokenOperations:
    """Test JWT token creation and verification"""
    
    def test_create_access_token(self):
        """Test access token creation"""
        email = "test@example.com"
        user_id = uuid4()
        expires_delta = timedelta(minutes=30)
        
        token = service.create_access_token(email, user_id, expires_delta)
        
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_verify_token_valid(self):
        """Test verification of a valid token"""
        email = "test@example.com"
        user_id = uuid4()
        expires_delta = timedelta(minutes=30)
        
        token = service.create_access_token(email, user_id, expires_delta)
        token_data = service.verify_token(token)
        
        assert isinstance(token_data, model.TokenData)
        assert token_data.user_id is not None
        assert str(token_data.user_id) == str(user_id)
    
    def test_verify_token_invalid(self):
        """Test verification of an invalid token"""
        invalid_token = "invalid.token.here"
        
        # FIX: Should expect an exception to be raised, not returned
        with pytest.raises(AuthenticationError):
            service.verify_token(invalid_token)
    
    def test_token_data_get_uuid(self):
        """Test TokenData.get_uuid() method"""
        user_id = uuid4()
        token_data = model.TokenData(user_id=user_id)
        
        uuid_result = token_data.get_uuid()
        assert uuid_result == user_id
    
    def test_token_data_get_uuid_none(self):
        """Test TokenData.get_uuid() returns None when user_id is None"""
        token_data = model.TokenData(user_id=None)
        
        uuid_result = token_data.get_uuid()
        assert uuid_result is None


class TestUserRegistration:
    """Test user registration"""
    
    def test_register_user_success(self, test_db):
        """Test successful user registration"""
        register_request = model.RegisterUserRequest(
            email="newuser@example.com",
            first_name="New",
            last_name="User",
            password="newpassword123"
        )
        
        service.register_user(test_db, register_request)
        
        # Verify user was created
        user = test_db.query(User).filter(User.email == "newuser@example.com").first()
        assert user is not None
        assert user.email == "newuser@example.com"
        assert user.first_name == "New"
        assert user.last_name == "User"
        assert user.password_hash != "newpassword123"  # Should be hashed
    
    def test_register_user_duplicate_email(self, test_db, test_user):
        """Test registration fails with duplicate email"""
        register_request = model.RegisterUserRequest(
            email="test@example.com",  # Already exists
            first_name="Another",
            last_name="User",
            password="password123"
        )
        
        with pytest.raises(Exception):
            service.register_user(test_db, register_request)


class TestLoginEndpoint:
    """Test login endpoint integration"""
    
    def test_login_success(self, client, test_user):
        """Test successful login"""
        response = client.post(
            "/auth/token",
            data={
                "username": "test@example.com",
                "password": "testpassword123"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "token_type" in data
        assert data["token_type"] == "bearer"
    
    def test_login_wrong_password(self, client, test_user):
        """Test login fails with wrong password"""
        response = client.post(
            "/auth/token",
            data={
                "username": "test@example.com",
                "password": "wrongpassword"
            }
        )
        
        assert response.status_code == 401
    
    def test_login_nonexistent_user(self, client):
        """Test login fails with non-existent user"""
        response = client.post(
            "/auth/token",
            data={
                "username": "nonexistent@example.com",
                "password": "anypassword"
            }
        )
        
        assert response.status_code == 401


class TestRegisterEndpoint:
    """Test register endpoint integration"""
    
    def test_register_endpoint_success(self, client, test_db):
        """Test successful registration via endpoint"""
        response = client.post(
            "/auth/",
            json={
                "email": "newuser@example.com",
                "first_name": "New",
                "last_name": "User",
                "password": "newpassword123"
            }
        )
        
        assert response.status_code == 201
        
        # Verify user was created
        user = test_db.query(User).filter(User.email == "newuser@example.com").first()
        assert user is not None
    
    def test_register_endpoint_invalid_email(self, client):
        """Test registration fails with invalid email"""
        response = client.post(
            "/auth/",
            json={
                "email": "invalidemail",
                "first_name": "New",
                "last_name": "User",
                "password": "newpassword123"
            }
        )
        
        assert response.status_code == 422  # Validation error