# This is the pytest file for Day_14/main.py
from fastapi.testclient import TestClient

from .main import app, todos

client = TestClient(app)

def setup_function():
    # Clear the mock database before each test
    todos.clear()

def test_read_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    response = client.post("/", json={"name": "Test Todo", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Todo", "completed": False}

def test_read_todo():
    client.post("/", json={"name": "Test Todo", "completed": False})
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Todo", "completed": False}

def test_update_todo():
    client.post("/", json={"name": "Test Todo", "completed": False})
    response = client.put("/1", json={"name": "Updated Todo", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Todo", "completed": True}

def test_delete_todo():
    client.post("/", json={"name": "Test Todo", "completed": False})
    response = client.delete("/1")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Todo", "completed": False}
    # Verify deletion
    response = client.get("/1")
    assert response.status_code == 404