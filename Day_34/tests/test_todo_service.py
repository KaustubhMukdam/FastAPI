import pytest
from datetime import datetime, timezone
from uuid import uuid4
from src.todos import service, model
from src.entities.todo import Todo, Priority
from src.exceptions import TodoNotFoundError, TodoCreationError
from src.auth.model import TokenData


class TestCreateTodo:
    """Test todo creation"""
    
    def test_create_todo_success(self, test_db, test_user):
        """Test successfully creating a todo"""
        current_user = TokenData(user_id=test_user.id)
        todo_create = model.TodoCreate(
            description="Test Todo",
            priority=Priority.Medium
        )
        
        created_todo = service.create_todo(current_user, test_db, todo_create)
        
        assert created_todo is not None
        assert created_todo.description == "Test Todo"
        assert created_todo.user_id == test_user.id
        assert created_todo.is_completed is False
        assert created_todo.priority == Priority.Medium
    
    def test_create_todo_with_due_date(self, test_db, test_user):
        """Test creating a todo with a due date"""
        current_user = TokenData(user_id=test_user.id)
        due_date = datetime(2025, 12, 31, 23, 59, 59)
        todo_create = model.TodoCreate(
            description="Todo with deadline",
            due_date=due_date,
            priority=Priority.High
        )
        
        created_todo = service.create_todo(current_user, test_db, todo_create)
        
        assert created_todo.due_date == due_date
        assert created_todo.priority == Priority.High
    
    def test_create_todo_default_priority(self, test_db, test_user):
        """Test that default priority is set correctly"""
        current_user = TokenData(user_id=test_user.id)
        todo_create = model.TodoCreate(
            description="Todo with default priority"
        )
        
        created_todo = service.create_todo(current_user, test_db, todo_create)
        
        assert created_todo.priority == Priority.Medium


class TestGetTodos:
    """Test getting todos"""
    
    def test_get_todos_empty(self, test_db, test_user):
        """Test getting todos when none exist"""
        current_user = TokenData(user_id=test_user.id)
        
        todos = service.get_todos(current_user, test_db)
        
        assert todos == []
    
    def test_get_todos_single(self, test_db, test_user, test_todo):
        """Test getting a single todo"""
        current_user = TokenData(user_id=test_user.id)
        
        todos = service.get_todos(current_user, test_db)
        
        assert len(todos) == 1
        assert todos[0].id == test_todo.id
        assert todos[0].description == test_todo.description
    
    def test_get_todos_multiple(self, test_db, test_user):
        """Test getting multiple todos"""
        current_user = TokenData(user_id=test_user.id)
        
        # Create multiple todos
        for i in range(3):
            todo = Todo(
                id=uuid4(),
                user_id=test_user.id,
                description=f"Todo {i}",
                is_completed=False
            )
            test_db.add(todo)
        test_db.commit()
        
        todos = service.get_todos(current_user, test_db)
        
        assert len(todos) == 3
    
    def test_get_todos_only_own(self, test_db, test_user, test_user_2):
        """Test that users only see their own todos"""
        current_user = TokenData(user_id=test_user.id)
        
        # Create todo for test_user
        todo1 = Todo(
            id=uuid4(),
            user_id=test_user.id,
            description="User 1 Todo",
            is_completed=False
        )
        test_db.add(todo1)
        
        # Create todo for test_user_2
        todo2 = Todo(
            id=uuid4(),
            user_id=test_user_2.id,
            description="User 2 Todo",
            is_completed=False
        )
        test_db.add(todo2)
        test_db.commit()
        
        todos = service.get_todos(current_user, test_db)
        
        assert len(todos) == 1
        assert todos[0].description == "User 1 Todo"


class TestGetTodoById:
    """Test getting a specific todo by ID"""
    
    def test_get_todo_by_id_success(self, test_db, test_user, test_todo):
        """Test successfully getting a todo by ID"""
        current_user = TokenData(user_id=test_user.id)
        
        todo = service.get_todo_by_id(current_user, test_db, test_todo.id)
        
        assert todo is not None
        assert todo.id == test_todo.id
        assert todo.description == test_todo.description
    
    def test_get_todo_by_id_not_found(self, test_db, test_user):
        """Test getting a non-existent todo raises TodoNotFoundError"""
        current_user = TokenData(user_id=test_user.id)
        non_existent_id = uuid4()
        
        with pytest.raises(TodoNotFoundError) as exc_info:
            service.get_todo_by_id(current_user, test_db, non_existent_id)
        
        assert exc_info.value.status_code == 404
    
    def test_get_todo_by_id_wrong_user(self, test_db, test_user, test_user_2):
        """Test that users cannot access other users' todos"""
        current_user = TokenData(user_id=test_user.id)
        
        # Create todo for test_user_2
        other_todo = Todo(
            id=uuid4(),
            user_id=test_user_2.id,
            description="Other user's todo",
            is_completed=False
        )
        test_db.add(other_todo)
        test_db.commit()
        
        with pytest.raises(TodoNotFoundError):
            service.get_todo_by_id(current_user, test_db, other_todo.id)


class TestUpdateTodo:
    """Test updating todos"""
    
    def test_update_todo_description(self, test_db, test_user, test_todo):
        """Test updating todo description"""
        current_user = TokenData(user_id=test_user.id)
        todo_update = model.TodoUpdate(
            description="Updated description"
        )
        
        updated_todo = service.update_todo(current_user, test_db, test_todo.id, todo_update)
        
        assert updated_todo.description == "Updated description"
    
    def test_update_todo_completion(self, test_db, test_user, test_todo):
        """Test updating todo completion status"""
        current_user = TokenData(user_id=test_user.id)
        todo_update = model.TodoUpdate(
            is_completed=True
        )
        
        updated_todo = service.update_todo(current_user, test_db, test_todo.id, todo_update)
        
        assert updated_todo.is_completed is True
    
    def test_update_todo_not_found(self, test_db, test_user):
        """Test updating non-existent todo raises TodoNotFoundError"""
        current_user = TokenData(user_id=test_user.id)
        non_existent_id = uuid4()
        todo_update = model.TodoUpdate(description="New description")
        
        with pytest.raises(TodoNotFoundError):
            service.update_todo(current_user, test_db, non_existent_id, todo_update)
    
    def test_update_todo_wrong_user(self, test_db, test_user, test_user_2):
        """Test that users cannot update other users' todos"""
        current_user = TokenData(user_id=test_user.id)
        
        # Create todo for test_user_2
        other_todo = Todo(
            id=uuid4(),
            user_id=test_user_2.id,
            description="Other user's todo",
            is_completed=False
        )
        test_db.add(other_todo)
        test_db.commit()
        
        todo_update = model.TodoUpdate(description="Hacked!")
        
        with pytest.raises(TodoNotFoundError):
            service.update_todo(current_user, test_db, other_todo.id, todo_update)


class TestCompleteTodo:
    """Test completing todos"""
    
    def test_complete_todo_success(self, test_db, test_user, test_todo):
        """Test successfully completing a todo"""
        current_user = TokenData(user_id=test_user.id)
        
        completed_todo = service.complete_todo(current_user, test_db, test_todo.id)
        
        assert completed_todo.is_completed is True
        assert completed_todo.completed_at is not None
    
    def test_complete_todo_not_found(self, test_db, test_user):
        """Test completing non-existent todo raises TodoNotFoundError"""
        current_user = TokenData(user_id=test_user.id)
        non_existent_id = uuid4()
        
        with pytest.raises(TodoNotFoundError):
            service.complete_todo(current_user, test_db, non_existent_id)


class TestDeleteTodo:
    """Test deleting todos"""
    
    def test_delete_todo_success(self, test_db, test_user, test_todo):
        """Test successfully deleting a todo"""
        current_user = TokenData(user_id=test_user.id)
        
        service.delete_todo(current_user, test_db, test_todo.id)
        
        # Verify todo is deleted
        todo = test_db.query(Todo).filter(Todo.id == test_todo.id).first()
        assert todo is None
    
    def test_delete_todo_not_found(self, test_db, test_user):
        """Test deleting non-existent todo raises TodoNotFoundError"""
        current_user = TokenData(user_id=test_user.id)
        non_existent_id = uuid4()
        
        with pytest.raises(TodoNotFoundError):
            service.delete_todo(current_user, test_db, non_existent_id)
    
    def test_delete_todo_wrong_user(self, test_db, test_user, test_user_2):
        """Test that users cannot delete other users' todos"""
        current_user = TokenData(user_id=test_user.id)
        
        # Create todo for test_user_2
        other_todo = Todo(
            id=uuid4(),
            user_id=test_user_2.id,
            description="Other user's todo",
            is_completed=False
        )
        test_db.add(other_todo)
        test_db.commit()
        
        with pytest.raises(TodoNotFoundError):
            service.delete_todo(current_user, test_db, other_todo.id)


class TestTodoEndpoints:
    """Test todo-related endpoints"""
    
    def test_create_todo_endpoint(self, client, auth_headers):
        """Test creating a todo via endpoint"""
        response = client.post(
            "/todos/",
            json={
                "description": "New todo from endpoint",
                "priority": 2  # Use enum value (Medium = 2) instead of string
            },
            headers=auth_headers
        )
        
        assert response.status_code == 201
        data = response.json()
        assert data["description"] == "New todo from endpoint"
        assert "id" in data
    
    def test_get_todos_endpoint(self, client, auth_headers, test_todo):
        """Test getting all todos via endpoint"""
        response = client.get("/todos/", headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1
    
    def test_get_todo_endpoint(self, client, auth_headers, test_todo):
        """Test getting a specific todo via endpoint"""
        response = client.get(f"/todos/{test_todo.id}", headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == str(test_todo.id)
        assert data["description"] == test_todo.description
    
    def test_update_todo_endpoint(self, client, auth_headers, test_todo):
        """Test updating a todo via endpoint"""
        response = client.put(
            f"/todos/{test_todo.id}",
            json={
                "description": "Updated via endpoint",
                "is_completed": True
            },
            headers=auth_headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["description"] == "Updated via endpoint"
    
    def test_delete_todo_endpoint(self, client, auth_headers, test_todo):
        """Test deleting a todo via endpoint"""
        response = client.delete(f"/todos/{test_todo.id}", headers=auth_headers)
        
        assert response.status_code == 204
    
    def test_endpoints_unauthorized(self, client):
        """Test that endpoints require authentication"""
        # Get all todos
        response = client.get("/todos/")
        assert response.status_code == 401
        
        # Create todo
        response = client.post("/todos/", json={"description": "test"})
        assert response.status_code == 401
        
        # Get specific todo
        response = client.get(f"/todos/{uuid4()}")
        assert response.status_code == 401
        
        # Update todo
        response = client.put(f"/todos/{uuid4()}", json={"description": "test"})
        assert response.status_code == 401
        
        # Delete todo
        response = client.delete(f"/todos/{uuid4()}")
        assert response.status_code == 401


class TestTodoModels:
    """Test todo model validations"""
    
    def test_todo_create_model(self):
        """Test TodoCreate model"""
        todo_create = model.TodoCreate(
            description="Test todo",
            priority=Priority.High
        )
        
        assert todo_create.description == "Test todo"
        assert todo_create.priority == Priority.High
        assert todo_create.due_date is None
    
    def test_todo_update_model(self):
        """Test TodoUpdate model"""
        todo_update = model.TodoUpdate(
            description="Updated description",
            is_completed=True
        )
        
        assert todo_update.description == "Updated description"
        assert todo_update.is_completed is True
    
    def test_todo_update_partial(self):
        """Test TodoUpdate model with partial data"""
        todo_update = model.TodoUpdate(
            description="Only description updated"
        )
        
        assert todo_update.description == "Only description updated"
        assert todo_update.is_completed is None
        assert todo_update.due_date is None