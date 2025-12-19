#This files contains the main FastAPI code which would manipulate data to be stored in SQLite

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from uuid import UUID
import models
from db import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)    #This will create the table if it does not exist

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Book(BaseModel):
    title : str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

BOOKS = []

@app.get("/")
def read_api(db_name: Session = Depends(get_db)):
    return db_name.query(models.Books).all()

@app.post("/")
def create_book(book : Book, db_name: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db_name.add(book_model)
    db_name.commit()
    db_name.refresh(book_model)
    return book_model

@app.put("/{book_id}")
def update_book(book_id : int, book : Book, db_name: Session = Depends(get_db)):
    book_model = db_name.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:  #This is called Guard Clause
        raise HTTPException(status_code=404, detail=f"Id of Book id: {book_id} does not exists")
    
    book_model.title = book.title
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating


    db_name.add(book_model)
    db_name.commit()
    db_name.refresh(book_model)
    return book_model

@app.delete("/{book_id}")
def delete_book(book_id : int, db_name: Session = Depends(get_db)):
    book_model = db_name.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:  #This is called Guard Clause
        raise HTTPException(status_code=404, detail=f"Id of Book id: {book_id} does not exists")


    db_name.query(models.Books).filter(models.Books.id == book_id).delete()
    db_name.commit()
