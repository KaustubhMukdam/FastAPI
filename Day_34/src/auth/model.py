from uuid import UUID
from pydantic import BaseModel, EmailStr

class RegisterUserRequest(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: UUID | None = None

    def get_uuid(self) -> UUID | None:
        if self.user_id is not None:
            return UUID(str(self.user_id))
        return None
    
class TodoCreate(BaseModel):
    description: str
    due_date: str | None = None
    priority: str | None = None