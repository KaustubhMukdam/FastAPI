from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Todo(BaseModel):
    name: str
    completed: bool

# Mock database
todos = {}

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get("/", response_model=List[Todo])
async def read_todos():
    return list(todos.values())

@app.get("/{todo_id}", response_model=Todo)
async def read_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# --- POST Request Methods ---
@app.post("/", response_model=Todo)
async def create_todo(todo: Todo):
    todo_id = str(len(todos) + 1)
    todos[todo_id] = todo
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

# --- PUT Request Methods ---
@app.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: Todo):
    todo = todos.get(str(todo_id))
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = updated_todo
    return updated_todo

# --- DELETE Request Methods ---
@app.delete("/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return todo
