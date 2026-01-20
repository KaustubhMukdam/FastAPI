from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Annotated
from datetime import timedelta, datetime, timezone
import app.exceptions as exceptions

from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)

db_dependency = Annotated[Session, Depends(get_db)]

# --- API Endpoints ---


# --- GET Request Methods ---
@router.get("/", response_model=List[schemas.Post])
def read_posts(
    db: db_dependency,
    skip: int = 0,
    limit: int = 10,
):
    posts = db.query(models.Post).order_by(models.Post.timestamp.desc()).offset(skip).limit(limit).all()
    return posts

@router.get("/with_counts/", response_model=List[schemas.PostWithCounts])
def read_posts_with_counts(
    db: db_dependency
):
    likes_subq = (
        db.query(models.Like.post_id, func.count(models.Like.post_id).label("like_count"))
        .group_by(models.Like.post_id)
        .subquery()
    )

    # Subquery to count retweets for each post
    retweets_subq = (
        db.query(models.Retweet.post_id, func.count(models.Retweet.post_id).label("retweet_count"))
        .group_by(models.Retweet.post_id)
        .subquery()
    )

    #Fetch posts along with their likes/retweet counts and owner username
    posts = (
        db.query(
            models.Post,
            models.User.username.label("owner_username"),
            func.coalesce(likes_subq.c.like_count, 0).label("like_count"),
            func.coalesce(retweets_subq.c.retweet_count, 0).label("retweet_count"),
        )
        .join(models.User, models.Post.owner_id == models.User.id)
        .outerjoin(likes_subq, models.Post.id == likes_subq.c.post_id)
        .outerjoin(retweets_subq, models.Post.id == retweets_subq.c.post_id)
        .order_by(models.Post.timestamp.desc())
        .all()
    )

    #Construct the response with posts, counts and owner username
    response_posts = []
    for post, owner_username, like_count, retweet_count in posts:
        response_post = schemas.PostWithCounts(
            id=post.id,
            content=post.content,
            timestamp=post.timestamp,
            owner_id = post.owner_id,
            owner_username=owner_username,
            like_count=like_count,
            retweet_count=retweet_count,
        )
        response_posts.append(response_post)
        return response_posts

# --- POST Request Methods ---
@router.post("/", response_model=schemas.Post)
def create_new_post(
    post: schemas.PostCreate,
    db: db_dependency,
    current_user: models.User = Depends(auth.get_current_user),
):
    db_post = models.Post(content=post.content, owner_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.post("/{post_id}/like", status_code=204)
def like_post(
    db: db_dependency,
    post_id: int,
    current_user: models.User = Depends(auth.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise exceptions.PostNotFoundException("Post not found.")
    new_like = models.Like(post_id=post_id, user_id=current_user.id)
    db.add(new_like)
    db.commit()
    return

@router.post("/{post_id}/unlike", status_code=204)
def unlike_post (
    db: db_dependency,
    post_id: int,
    current_user: models.User = Depends(auth.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise exceptions.PostNotFoundException("Post not found.")
    like = db.query(models.Like).filter(models.Like.post_id == post_id, models.Like.user_id == current_user.id).first()
    if like is None:
        raise exceptions.LikeNotFoundException("Like not found.")
    db.delete(like)
    db.commit()
    return

@router.post("/{post_id}/retweet", status_code=204)
def retweet_post(
    db: db_dependency,
    post_id: int,
    current_user: models.User = Depends(auth.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise exceptions.PostNotFoundException("Post not found.")
    new_retweet = models.Retweet(post_id=post_id, user_id=current_user.id)
    db.add(new_retweet)
    db.commit()
    return

@router.post("/{post_id}/unretweet", status_code=204)
def unretweet_post (
    db: db_dependency,
    post_id: int,
    current_user: models.User = Depends(auth.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise exceptions.PostNotFoundException("Post not found.")
    retweet = db.query(models.Retweet).filter(models.Retweet.post_id == post_id, models.Retweet.user_id == current_user.id).first()
    if retweet is None:
        raise exceptions.RetweetNotFoundException("Retweet not found.")
    db.delete(retweet)
    db.commit()
    return

# --- PUT Request Methods ---
@router.put("/{post_id}", response_model=schemas.Post)
def update_post(
    post_id: int,
    post_update: schemas.PostUpdate,
    db: db_dependency,
    current_user: models.User = Depends(auth.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise exceptions.PostNotFoundException("Post not found.")
    if post.owner_id != current_user.id:
        raise exceptions.UnauthorizedException("You are not authorized to update this post.")
    
    # Check if the post is within the 10-minutes edit window
    post_timestamp_aware = post.timestamp.replace(tzinfo=timezone.utc)
    time_since_creation = datetime.now(timezone.utc) - post_timestamp_aware
    if time_since_creation > timedelta(minutes=10):
        raise exceptions.ForbiddenException("You are not allowed to update this post.")
    
    post.content = post_update.content
    db.commit()
    db.refresh(post)
    return post


# --- DELETE Request Methods ---
@router.delete("/{post_id}", status_code=204)
def delete_existing_post(
    post_id: int,
    db: db_dependency,
    current_user: models.User = Depends(auth.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise exceptions.PostNotFoundException("Post not found.")
    if post.owner_id != current_user.id:
        raise exceptions.UnauthorizedException("You are not authorized to delete this post.")
    db.delete(post)
    db.commit()