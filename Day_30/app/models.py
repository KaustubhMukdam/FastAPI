from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone


follow = Table(
    "follows",
    Base.metadata,
    Column("follower_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("followee_id", Integer, ForeignKey("users.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(250), unique=True, index=True, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    posts = relationship("Post", back_populates="owner")

    followers = relationship(
        "User",
        secondary=follow,
        primaryjoin=id == follow.c.follower_id,
        secondaryjoin=id == follow.c.followee_id,
        backref="following",
    )

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(500), nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="posts")
    likes = relationship("Like", back_populates="post")
    retweets = relationship("Retweet", back_populates="post")

class Like(Base):
    __tablename__ = "likes"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    user = relationship("User")
    post = relationship("Post", back_populates="likes")

class Retweet(Base):
    __tablename__ = "retweets"
    
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True, nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    user = relationship("User")
    post = relationship("Post", back_populates="retweets")
