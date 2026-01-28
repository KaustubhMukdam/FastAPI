from fastapi import HTTPException

class TodoError(HTTPException):
    pass

class TodoNotFoundError(TodoError):
    def __init__(self, todo_id=None):
        super().__init__(status_code=404, detail=f"Todo with ID {todo_id} not found.")

class TodoCreationError(TodoError):
    def __init__(self, message="Failed to create todo."):
        super().__init__(status_code=500, detail=message)

class UserError(HTTPException):
    pass

class UserNotFoundError(UserError):
    def __init__(self, user_id=None):
        super().__init__(status_code=404, detail=f"User with ID {user_id} not found.")

class PasswordMismatchError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="New password and confirmation do not match.")

class InvalidPasswordError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="The current password is incorrect.")

class AuthenticationError(HTTPException):
    def __init__(self, message="Authentication failed."):
        super().__init__(status_code=401, detail=message)