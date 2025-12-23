# Creates the tables/models for the MySQL database (with the help of SQLAlchemy)

from sqlalchemy import Boolean, Column, Integer, String
from mysqldatabase import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    content = Column(String(500))
    user_id = Column(Integer)