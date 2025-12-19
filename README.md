# FastAPI
## Youtube Link: https://youtube.com/playlist?list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq_&si=I-iGQjf2HPXqzxW4

# Day-1:
## creating RESTFul API using FastAPI
Firstly we need to install 2 things
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
uvicorn is an ASGI server which would run our programs

RestFul API uses the http requests
popular requests methods are
GET, POST, PUT, PATCH, DELETE
GET: Read Resource
POST: Create Resource
PUT: Update/Replace Resource
DELETE: Delete Resource

---
# Day-2
## Connecting Database with FastAPI to store details of books
For this we would be using SQLAlchemy and SQLite
SQLAlchemy is an Object Relational Mapper (ORM) for python which allows us to map Python objects to SQL tables and vice versa
SQLite is a database that stores data in a file, which is used to store data in a local database

Here we perform CRUD operations on our database
We need to install 2 things
1. sqlalchemy: pip install sqlalchemy
2. SQLite
---