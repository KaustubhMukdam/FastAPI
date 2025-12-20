from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id : UUID
    title : str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

BOOKS = []

@app.get("/")
def read_api():
    return BOOKS

#Path/Query parameter: It is used to pass the value in the url
# @app.get("/{name}")
# def read_name_api(name):
#     return { "Welcome" : name }

@app.post("/")
def create_book(book : Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id : UUID, book : Book):
    count = 0
    for x in BOOKS:
        count += 1
        if x.id == book_id:
            BOOKS[count - 1] = book
            return BOOKS[count - 1]
        
    raise HTTPException(status_code=404, detail=f"Id of Book id: {book_id} does not exists")

@app.delete("/{book_id}")
def delete_book(book_id : UUID):
    count = 0
    for x in BOOKS:
        count += 1
        if x.id == book_id:
            del BOOKS[count - 1]
            return f"Book with id: {book_id} deleted"
        
    raise HTTPException(status_code=404, detail=f"Id of Book id: {book_id} does not exists")


read_api()