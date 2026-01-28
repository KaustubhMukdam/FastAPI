from datetime import datetime, timezone
from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import model
from src.auth.model import TokenData
from src.entities.todo import Todo
from src.exceptions import TodoCreationError, TodoNotFoundError
import logging

def create_todo(current_user: TokenData, db: Session, todo: model.TodoCreate) -> Todo:
    try:
        new_todo = Todo(**todo.model_dump())
        new_todo.user_id = current_user.get_uuid()
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        logging.info(f"Successfully created todo with ID: {new_todo.id}")
        return new_todo
    except Exception as e:
        logging.error(f"Error creating todo: {e}")
        raise TodoCreationError(str(e))
    
def get_todos(current_user: TokenData, db: Session) -> list[model.TodoResponse]:
    todos = db.query(Todo).filter(Todo.user_id == current_user.get_uuid()).all()
    logging.info(f"Retrieved {len(todos)} todos for user with ID: {current_user.get_uuid()}")
    return todos

def get_todo_by_id(current_user: TokenData, db: Session, todo_id: UUID) -> Todo:
    todo = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.user_id == current_user.get_uuid()).first()
    if todo is None:
        logging.warning(f"Todo not found with ID: {todo_id}")
        raise TodoNotFoundError(todo_id)
    logging.info(f"Successfully retrieved todo with ID: {todo_id}")
    return todo

def update_todo(current_user: TokenData, db: Session, todo_id: UUID, todo: model.TodoUpdate) -> Todo:
    todo_to_update = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.user_id == current_user.get_uuid()).first()
    if todo_to_update is None:
        logging.warning(f"Todo not found with ID: {todo_id}")
        raise TodoNotFoundError(todo_id)
    if todo.description is not None:
        todo_to_update.description = todo.description
    if todo.is_completed is not None:
        todo_to_update.is_completed = todo.is_completed
    if todo.due_date is not None:
        todo_to_update.due_date = todo.due_date
    if todo.priority is not None:
        todo_to_update.priority = todo.priority
    db.commit()
    db.refresh(todo_to_update)
    logging.info(f"Successfully updated todo with ID: {todo_id}")
    return todo_to_update

def complete_todo(current_user: TokenData, db: Session, todo_id: UUID) -> Todo:
    todo_to_complete = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.user_id == current_user.get_uuid()).first()
    if todo_to_complete is None:
        logging.warning(f"Todo not found with ID: {todo_id}")
        raise TodoNotFoundError(todo_id)
    todo_to_complete.is_completed = True
    todo_to_complete.completed_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(todo_to_complete)
    logging.info(f"Successfully completed todo with ID: {todo_id}")
    return todo_to_complete

def delete_todo(current_user: TokenData, db: Session, todo_id: UUID) -> None:
    todo_to_delete = db.query(Todo).filter(Todo.id == todo_id).filter(Todo.user_id == current_user.get_uuid()).first()
    if todo_to_delete is None:
        logging.warning(f"Todo not found with ID: {todo_id}")
        raise TodoNotFoundError(todo_id)
    db.delete(todo_to_delete)
    db.commit()
    logging.info(f"Successfully deleted todo with ID: {todo_id}")