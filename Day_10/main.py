from fastapi import FastAPI, status
from pydantic import BaseModel, Field, field_validator, EmailStr
from uuid import UUID, uuid4

app = FastAPI()

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=5, max_length=12)  #min and max length are for strings
    age: int = Field(gt=12, lt=100)

    # Example Schema extra
    class Config:
        json_schema_extra = {
            "example": {
                "email": "test@example.com",
                "password": "test123",
                "age": 25
            }
        }

    #Field Validator example
    @field_validator("password")
    def password_validator(cls, value):
        if value == "test123":
            raise ValueError("Password cannot be 'test123'")
        return value
    
    @field_validator("email")
    def email_validator(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        if value == "test@example.com":
            raise ValueError("Email cannot be 'test@example.com'")
        return value

class User(UserCreate):
    id: UUID = Field(default_factory=uuid4)

# --- API Endpoints ---

# --- GET Request Methods ---


# --- POST Request Methods ---
@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    created_user = User(email=user.email, password=user.password, age=user.age)
    return created_user

# A better way is to use model_dump to convert Pydantic models to dictionaries
@app.post("/users/dict/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_dict(user: UserCreate):
    user_data = user.model_dump()
    created_user = User(**user_data)
    return created_user