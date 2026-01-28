from fastapi import APIRouter, status
from typing import List
from uuid import UUID

from ..database.core import DBSession
from . import model, service
from ..auth.service import CurrentUser

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# --- API Endpoints ---

# --- GET Request Methods ---
@router.get("/", response_model=List[model.TodoResponse])
def get_todos(current_user: CurrentUser, db: DBSession):
    return service.get_todos(current_user, db)

@router.get("/{todo_id}", response_model=model.TodoResponse)
def get_todo(db: DBSession, current_user: CurrentUser, todo_id: UUID):
    return service.get_todo_by_id(current_user, db, todo_id)


# --- POST Request Methods ---
@router.post("/", response_model=model.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(db: DBSession, current_user: CurrentUser, todo: model.TodoCreate):
    return service.create_todo(current_user, db, todo)

# --- PUT Request Methods ---
@router.put("/{todo_id}", response_model=model.TodoResponse)
def update_todo(
    todo_id: UUID,
    todo: model.TodoUpdate,
    db: DBSession,
    current_user: CurrentUser
):
    return service.update_todo(current_user, db, todo_id, todo)

# --- DELETE Request Methods ---
@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(
    todo_id: UUID,
    db: DBSession,
    current_user: CurrentUser
):
    service.delete_todo(current_user, db, todo_id)