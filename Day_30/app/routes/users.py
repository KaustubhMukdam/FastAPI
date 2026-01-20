from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app import models, schemas, auth
from ..database import get_db
from ..exceptions import (
    raise_not_found_exception,
    raise_bad_request_exception,
    raise_conflict_exception,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

db_dependency = Annotated[Session, Depends(get_db)]

# --- API Endpoints ---


# --- GET Request Methods ---


# --- POST Request Methods ---
@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: db_dependency = db_dependency):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise_conflict_exception("A user with this email already exists.")
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(
        username = user.username,
        email = user.email,
        hashed_password = hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/{user_id}/follow", status_code=204)
def follow_user(
    user_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: db_dependency = db_dependency,
):
    user_to_follow = db.query(models.User).filter(models.User.id == user_id).first()
    if user_to_follow is None:
        raise_not_found_exception("User to follow not found.")
    if user_to_follow == current_user:
        raise_bad_request_exception("You cannot follow yourself.")
    if user_to_follow in current_user.following:
        raise_bad_request_exception("You are already following this user.")
    current_user.following.append(user_to_follow)
    db.commit()
    return

@router.post("/{user_id}/unfollow", status_code=204)
def unfollow_user(
    user_id: int,
    current_user: models.User = Depends(auth.get_current_user),
    db: db_dependency = db_dependency,
):
    user_to_unfollow = db.query(models.User).filter(models.User.id == user_id).first()
    if user_to_unfollow is None:
        raise_not_found_exception("User to unfollow not found.")
    if user_to_unfollow == current_user:
        raise_bad_request_exception("You cannot unfollow yourself.")
    if user_to_unfollow not in current_user.following:
        raise_bad_request_exception("You are not following this user.")
    current_user.following.remove(user_to_unfollow)
    db.commit()
    return
