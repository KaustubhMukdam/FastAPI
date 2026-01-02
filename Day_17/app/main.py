from enum import unique

from fastapi import FastAPI, BackgroundTasks, Depends
from typing import Annotated
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

app = FastAPI()

# Database Configuration: SQLite
DATABASE_URL = "sqlite:///./test_17.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Define a simple User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

# Initialize our database
Base.metadata.create_all(bind=engine)

# --- API endpoints ---

# --- GET Request Methods ---
@app.get("/user/")
async def get_users(db: db_dependency):
    return db.query(User).all()

# --- POST Request Methods ---
@app.post("/user/")
async def create_user(name: str, background_tasks: BackgroundTasks, db: db_dependency):
    user = User(name = name)
    db.add(user)
    db.commit()
    background_tasks.add_task(print_message, name)
    return {"name": name, "message": "User created successfully!"}

async def print_message(name: str):
    print(f"User {name} created successfully!")

