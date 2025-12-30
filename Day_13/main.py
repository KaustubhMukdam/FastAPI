from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine, text
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

load_dotenv()

Database_URL = os.getenv("SQLite_Database_URL")

Base: DeclarativeMeta = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

engine = create_engine(
    Database_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API Endpoints ---

# --- GET Request Methods ---


# --- POST Request Methods ---
@app.post("/register/")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user_id": new_user.id}

@app.post("/signin/")
def signin_user(username: str, password: str, db: Session = Depends(get_db)):
    #query = text(f"SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")  #This is vulnerable to SQL Injection
    query = text(f"SELECT * FROM users WHERE username = :username AND password = :password")    #This is secure
    result = db.execute(query, {"username": username, "password": password}).fetchone()
    if result is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"username": result[1], "message": "Signin successful"}