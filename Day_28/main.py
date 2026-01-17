from pydantic import BaseModel, Field, EmailStr, field_validator
import re
# BaseModel: Base class for all pydantic models
# Field: It works like a data validator

# class User():
#     def __init__(self, name, age, height):
#         self.name = name,
#         self.age = age,
#         self.height = height

#     def __repr__(self):
#         return f"User Attributes: Name: {self.name}, Age: {self.age}, Height: {self.height}"
    
# def main() -> None:
#     user = User("Kaustubh Mukdam", 21, 6.2)
#     print(user)

# if __name__ == "__main__":
#     main()

# Instead of writing this all the time we can use pydantic

usernames = ["kaustubh", "mukdam"]

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=18)
    height: int = Field(gt=40, lt=70)
    email: EmailStr
    username: str = Field(min_length=3, max_length=20)

    @field_validator("username")
    def validate_username(cls, value):
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username must contain only letters, numbers, and underscores")
        if value in usernames:
            raise ValueError("Username must be unique")
        
        usernames.append(value)
        
        return value

def main() -> None:
    user = User(name="Kaustubh Mukdam", age=21, height=60, email="test@example.com", username="KDM221005")
    print(user)

if __name__ == "__main__":
    main()