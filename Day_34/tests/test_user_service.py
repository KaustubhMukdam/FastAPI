import pytest
from uuid import uuid4
from src.users import service, model
from src.entities.user import User
from src.exceptions import UserNotFoundError, PasswordMismatchError, InvalidPasswordError
from src.auth.service import get_password_hash, verify_password


class TestGetUserById:
    """Test getting user by ID"""
    
    def test_get_user_by_id_success(self, test_db, test_user):
        """Test successfully getting a user by ID"""
        user = service.get_user_by_id(test_db, test_user.id)
        
        assert user is not None
        assert user.id == test_user.id
        assert user.email == test_user.email
        assert user.first_name == test_user.first_name
        assert user.last_name == test_user.last_name
    
    def test_get_user_by_id_not_found(self, test_db):
        """Test getting a non-existent user raises UserNotFoundError"""
        non_existent_id = uuid4()
        
        with pytest.raises(UserNotFoundError) as exc_info:
            service.get_user_by_id(test_db, non_existent_id)
        
        assert exc_info.value.status_code == 404


class TestChangePassword:
    """Test password change functionality"""
    
    def test_change_password_success(self, test_db, test_user):
        """Test successful password change"""
        password_change = model.PasswordChange(
            current_password="testpassword123",
            new_password="newpassword456",
            new_password_confirm="newpassword456"
        )
        
        service.change_password(test_db, test_user.id, password_change)
        
        # Refresh user from database
        test_db.refresh(test_user)
        
        # Verify new password works
        assert verify_password("newpassword456", test_user.password_hash) is True
        # Verify old password doesn't work
        assert verify_password("testpassword123", test_user.password_hash) is False
    
    def test_change_password_wrong_current_password(self, test_db, test_user):
        """Test password change fails with wrong current password"""
        password_change = model.PasswordChange(
            current_password="wrongpassword",
            new_password="newpassword456",
            new_password_confirm="newpassword456"
        )
        
        with pytest.raises(InvalidPasswordError) as exc_info:
            service.change_password(test_db, test_user.id, password_change)
        
        assert exc_info.value.status_code == 400
    
    def test_change_password_mismatch(self, test_db, test_user):
        """Test password change fails when new passwords don't match"""
        password_change = model.PasswordChange(
            current_password="testpassword123",
            new_password="newpassword456",
            new_password_confirm="differentpassword789"
        )
        
        with pytest.raises(PasswordMismatchError) as exc_info:
            service.change_password(test_db, test_user.id, password_change)
        
        assert exc_info.value.status_code == 400
    
    def test_change_password_user_not_found(self, test_db):
        """Test password change fails for non-existent user"""
        non_existent_id = uuid4()
        password_change = model.PasswordChange(
            current_password="testpassword123",
            new_password="newpassword456",
            new_password_confirm="newpassword456"
        )
        
        with pytest.raises(UserNotFoundError):
            service.change_password(test_db, non_existent_id, password_change)


class TestUserEndpoints:
    """Test user-related endpoints"""
    
    def test_get_current_user_success(self, client, test_user, auth_headers):
        """Test getting current user information"""
        response = client.get("/users/me", headers=auth_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["email"] == test_user.email
        assert data["first_name"] == test_user.first_name
        assert data["last_name"] == test_user.last_name
        assert data["id"] == str(test_user.id)
    
    def test_get_current_user_unauthorized(self, client):
        """Test getting current user fails without authentication"""
        response = client.get("/users/me")
        
        assert response.status_code == 401
    
    def test_get_current_user_invalid_token(self, client):
        """Test getting current user fails with invalid token"""
        headers = {"Authorization": "Bearer invalid_token"}
        response = client.get("/users/me", headers=headers)
        
        assert response.status_code == 401
    
    def test_change_password_endpoint_success(self, client, test_user, auth_headers):
        """Test password change endpoint"""
        response = client.put(
            "/users/change-password",
            json={
                "current_password": "testpassword123",
                "new_password": "newpassword456",
                "new_password_confirm": "newpassword456"
            },
            headers=auth_headers
        )
        
        assert response.status_code == 200
        
        # Verify can login with new password
        login_response = client.post(
            "/auth/token",
            data={
                "username": "test@example.com",
                "password": "newpassword456"
            }
        )
        assert login_response.status_code == 200
    
    def test_change_password_endpoint_wrong_current(self, client, test_user, auth_headers):
        """Test password change fails with wrong current password"""
        response = client.put(
            "/users/change-password",
            json={
                "current_password": "wrongpassword",
                "new_password": "newpassword456",
                "new_password_confirm": "newpassword456"
            },
            headers=auth_headers
        )
        
        assert response.status_code == 400
    
    def test_change_password_endpoint_mismatch(self, client, test_user, auth_headers):
        """Test password change fails when new passwords don't match"""
        response = client.put(
            "/users/change-password",
            json={
                "current_password": "testpassword123",
                "new_password": "newpassword456",
                "new_password_confirm": "differentpassword"
            },
            headers=auth_headers
        )
        
        assert response.status_code == 400
    
    def test_change_password_endpoint_unauthorized(self, client):
        """Test password change fails without authentication"""
        response = client.put(
            "/users/change-password",
            json={
                "current_password": "testpassword123",
                "new_password": "newpassword456",
                "new_password_confirm": "newpassword456"
            }
        )
        
        assert response.status_code == 401


class TestUserModels:
    """Test user model validations"""
    
    def test_user_response_model(self):
        """Test UserResponse model creation"""
        user_data = {
            "id": uuid4(),
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User"
        }
        
        user_response = model.UserResponse(**user_data)
        
        assert user_response.email == "test@example.com"
        assert user_response.first_name == "Test"
        assert user_response.last_name == "User"
    
    def test_user_response_invalid_email(self):
        """Test UserResponse model validates email"""
        user_data = {
            "id": uuid4(),
            "email": "invalidemail",  # Invalid email format
            "first_name": "Test",
            "last_name": "User"
        }
        
        with pytest.raises(Exception):  # Pydantic validation error
            model.UserResponse(**user_data)
    
    def test_password_change_model(self):
        """Test PasswordChange model creation"""
        password_change = model.PasswordChange(
            current_password="oldpass",
            new_password="newpass",
            new_password_confirm="newpass"
        )
        
        assert password_change.current_password == "oldpass"
        assert password_change.new_password == "newpass"
        assert password_change.new_password_confirm == "newpass"