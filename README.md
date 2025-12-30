# FastAPI
## Youtube Link: https://youtube.com/playlist?list=PLK8U0kF0E_D6l19LhOGWhVZ3sQ6ujJKq_&si=I-iGQjf2HPXqzxW4

# Day-1:
## creating RESTFul API using FastAPI (Folder: Day_1)
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

To run the application:
uvicorn Day_1.restful:app --reload

### Files:
restful.py: Contains the FastAPI application code

---
# Day-2
## Connecting Database with FastAPI to store details of books (Folder: Day_2)
For this we would be using SQLAlchemy and SQLite
SQLAlchemy is an Object Relational Mapper (ORM) for python which allows us to map Python objects to SQL tables and vice versa
SQLite is a database that stores data in a file, which is used to store data in a local database

Here we perform CRUD operations on our database
We need to install 2 things
1. sqlalchemy: pip install sqlalchemy
2. SQLite

### Files:
database.py: Contains the FastAPI application code
db.py: Contains the database code
models.py: Contains the database models
---
# Day-3

## FastAPI Application with NoSQL Database (MongoDB) (Folder: Day_3)
For this we would be using MongoDB
MongoDB is a NoSQL database which stores data in a JSON format

For using MongoDB, we would be using Atlas which is a cloud service for MongoDB

We need to install the following:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. pymongo: pip install pymongo

To run the application:
uvicorn Day_3.mongo:app --reload

### Files:
mongo.py: Contains the FastAPI application code
config/mongo_db.py: Contains the MongoDB connection code
models/mongo_models.py: Contains the MongoDB models
schema/schemas.py: Contains the Pydantic schemas
routes/route.py: Contains the API routes

---
# Day-4

## FastAPI Application with PostgreSQL Database (Folder: Day_4)
Today we would be creating a quiz game using FastAPI and PostgreSQL. This application allows creating questions with multiple choices and retrieving them via API endpoints.

We need to install the following:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. sqlalchemy: pip install sqlalchemy
4. psycopg2-binary: pip install psycopg2-binary (for PostgreSQL connection)
5. python-dotenv: pip install python-dotenv

Ensure you have a PostgreSQL database set up and configure the POSTGRES_DATABASE_URL in a .env file.

To run the application:
uvicorn Day_4.quiz:app --reload

### Files:
database.py: Contains the database connection setup using SQLAlchemy and PostgreSQL.
models.py: Contains the SQLAlchemy models for Questions and Choices tables.
quiz.py: Contains the FastAPI application code with API endpoints for the quiz game.

---
# Day-5

## FastAPI Application with MySQL Database (Folder: Day_5)
Today we would be creating a blog application using FastAPI and MySQL. This application allows creating users and blog posts, retrieving them, and deleting them via API endpoints.

We need to install the following libraries:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. sqlalchemy: pip install sqlalchemy
4. pymysql: pip install pymysql (for MySQL connection)
5. python-dotenv: pip install python-dotenv

Ensure you have a MySQL database set up and configure the environment variables (MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE_NAME) in a .env file.

To run the application:
uvicorn Day_5.blog:app --reload

### API Endpoints:
- GET /users/{user_id}: Retrieve a user by ID
- GET /posts/{post_id}: Retrieve a post by ID
- POST /users/: Create a new user
- POST /posts/: Create a new post
- DELETE /users/{user_id}: Delete a user by ID
- DELETE /posts/{post_id}: Delete a post by ID

### Files:
mysqldatabase.py: Contains the MySQL database connection setup using SQLAlchemy.
models.py: Contains the SQLAlchemy models for User and Post tables.
blog.py: Contains the FastAPI application code with API endpoints for the blog.

---
# Day-6

## Finance App - FastAPI with React and SQLite (Folder: Day_6)
A full-stack finance application that combines FastAPI backend with React frontend, using SQLite as the database. This application allows users to track their income and expenses with transaction management.

We need to install the following libraries:

### Backend (FastAPI):
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. sqlalchemy: `pip install sqlalchemy`

### Frontend (React):
1. react: Built with Create React App
2. axios: For making HTTP requests to the backend API

### Database:
SQLite - A lightweight, file-based database (finance.db)

### Running the Application:

**Backend (FastAPI Server):**
```bash
cd Day_6/FastAPI
uvicorn main:app --reload
```
Backend runs on: `http://localhost:8000`

**Frontend (React App):**
```bash
cd Day_6/React/finance-app
npm install
npm start
```
Frontend runs on: `http://localhost:3000`

### API Endpoints:
- `GET /transactions`: Retrieve all transactions with pagination support (skip, limit parameters)
- `POST /transactions`: Create a new transaction

### Transaction Object Structure:
```json
{
  "amount": 100.50,
  "category": "Food",
  "description": "Groceries",
  "is_income": false,
  "date": "2024-12-24"
}
```

### Backend Files:
- **main.py**: Contains the FastAPI application code with API endpoints and CORS middleware configuration
- **models.py**: Contains the SQLAlchemy model for the Transaction table
- **database.py**: Contains the SQLite database connection setup using SQLAlchemy
- **finance.db**: SQLite database file that stores all transaction data

### Frontend Files:
- **App.js**: Main React component that handles transaction display and form submission
- **api.js**: Axios API client for communicating with the FastAPI backend
- **App.css**: Styling for the application
- **index.js**: React application entry point

### Features:
- View all financial transactions
- Add new income/expense transactions with categories
- Track transaction details (amount, category, description, date)
- Real-time updates between frontend and backend
- Responsive UI with Bootstrap styling
- CORS enabled for frontend-backend communication

---
# Day-7

## FastAPI Application with Jinja2 Templates (Folder: Day_7)
An introduction to server-side rendering with FastAPI using Jinja2 templating engine. This application demonstrates how to render HTML templates dynamically with data passed from the backend.

We need to install the following:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. jinja2: `pip install jinja2`

### Running the Application:
```bash
cd Day_7
uvicorn main:app --reload
```
Application runs on: `http://localhost:8000`

### API Endpoints:
- `GET /`: Render the home page with Formula 1 drivers data

### Features:
- **Jinja2 Templates**: Server-side rendering of HTML templates
- **Dynamic Content**: Pass Python data to HTML templates
- **Template Loops**: Use Jinja2 for loops to iterate through data
- **Bootstrap Styling**: Responsive UI with Bootstrap 5

### Data Structure:
The application includes a list of Formula 1 drivers with their team information:
```python
F1 = [
    {"name": "Max Verstappen", "team": "Red Bull"},
    {"name": "Lewis Hamilton", "team": "Ferrari"},
    {"name": "Charles Leclerc", "team": "Ferrari"},
    {"name": "Kimi Antonelli", "team": "Mercedes"},
    {"name": "Sergio Perez", "team": "Red Bull"}
]
```

### Files:
- **main.py**: Contains the FastAPI application code with Jinja2 template configuration and route to render the home page
- **templates/home.html**: Jinja2 HTML template that displays a welcome message and a table of Formula 1 drivers with their teams

### Template Syntax Used:
- `{{ variable }}`: Display variable values in the template
- `{% for item in list %}...{% endfor %}`: Loop through data in templates
- `{{ item['key'] }}`: Access dictionary values in templates

---
# Day-8

## Deploying FastAPI to AWS Lambda (Folder: Day_8)
Learn how to deploy a FastAPI application to AWS Lambda using Mangum. Mangum is an ASGI adapter that allows FastAPI applications to run on AWS Lambda and other serverless platforms.

We need to install the following:
1. fastapi: `pip install fastapi`
2. mangum: `pip install mangum`

### What is Mangum?
Mangum is an ASGI adapter for AWS Lambda that allows you to deploy FastAPI applications serverlessly. It handles the conversion between AWS Lambda events and ASGI requests.

### Running Locally:
```bash
cd Day_8
uvicorn main:app --reload
```
Application runs on: `http://localhost:8000`

### API Endpoints:
- `GET /`: Returns a welcome message

### Deployment to AWS Lambda:

#### Step 1: Install Dependencies
```bash
pip3 install -t Day_8\dependencies -r requirements.txt
```
This installs all required dependencies into a local `dependencies` folder.

#### Step 2: Create ZIP Package for Lambda
Navigate to the Day_8 directory and compress the dependencies:
```bash
cd Day_8
cd dependencies
Compress-Archive -Path * -DestinationPath ..\lambda.zip -Force
cd ..
```

#### Step 3: Add Main Code to ZIP
Add the main.py file to the lambda.zip:
```bash
Compress-Archive -Path main.py -DestinationPath .\lambda.zip -Force
```

#### Step 4: Upload to AWS Lambda
- Go to AWS Lambda Console
- Create a new function
- Upload the `lambda.zip` file
- Set the handler to `main.handler`
- Configure environment variables and other settings as needed
- Deploy and test

### Files:
- **main.py**: Contains the FastAPI application with Mangum adapter. The `handler` variable is the entry point for AWS Lambda
- **dependencies/**: Directory containing all installed Python dependencies for the Lambda environment
- **lambda.zip**: Compressed package containing both the application code and dependencies, ready for AWS Lambda deployment

### Key Components:
```python
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)  # This is the Lambda handler
```

### Important Notes:
- The `handler = Mangum(app)` line creates the Lambda handler that AWS uses to process requests
- All dependencies must be included in the ZIP file for Lambda to find them
- The handler path in AWS Lambda should be set to `main.handler`
- Cold start times may be higher due to Lambda's execution model

### Features:
- **Serverless Deployment**: Deploy FastAPI without managing servers
- **Cost Efficient**: Pay only for execution time
- **Scalable**: Automatically scales with demand
- **ASGI Compatible**: Mangum provides full ASGI compatibility with Lambda

---
# Day-9

## FastAPI with JWT (JSON Web Token) Authentication (Folder: Day_9)

This module demonstrates how to secure FastAPI endpoints using JWT authentication with a SQLite database for user storage. It includes user registration, password hashing, token issuance (login), and token-protected routes.

You will typically need the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. python-jose: `pip install python-jose[cryptography]` (for JWT encoding/decoding)
4. passlib[bcrypt]: `pip install passlib[bcrypt]` (for password hashing)
5. sqlalchemy: `pip install sqlalchemy`

### Running the Application:
```bash
cd Day_9
uvicorn main:app --reload
```
Application runs on: `http://localhost:8000`

### Typical API Endpoints:
- `POST /register` : Create a new user (hashes password and stores user in SQLite)
- `POST /login` : Authenticate user credentials and return an access JWT
- `GET /protected` : Example protected route that requires a valid JWT in the `Authorization: Bearer <token>` header

### Security Notes:
- Use `python-jose` for secure JWT signing and verification.
- Store a strong secret key in environment variables (do not hardcode in source).
- Use secure password hashing (e.g., `passlib` with bcrypt).
- Consider token expiration and refresh strategies for production systems.

### Files:
- **auth.py**: Contains authentication helpers (password hashing, token creation, dependency to verify tokens)
- **database.py**: Database setup using SQLAlchemy and SQLite connection
- **models.py**: SQLAlchemy models for `User` (username, hashed_password, etc.)
- **main.py**: FastAPI application wiring routes and authentication dependencies

### Example token creation (concept):
```python
from jose import jwt

payload = {"sub": username}
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

### Example protected route (concept):
```python
from fastapi import Depends

@app.get('/protected')
def protected_route(current_user=Depends(get_current_user)):
  return {"message": f"Hello {current_user.username}"}
```

---
# Day-10
## Pydantic: A backbone of FastAPI (Folder: Day_10)
Pydantic is a data validation and serialization library for Python that serves as the backbone of FastAPI. It provides a simple and efficient way to define data models, validate input/output, and handle data parsing.

Key Features Demonstrated:
1. **Field Validation**: Using Field constraints like min_length, max_length, gt, lt for data validation

2. **Dynamic UUID**: Generating unique IDs using default_factory with uuid4

3. **Populate JSON to Python Objects**: Converting Pydantic models to dictionaries using model_dump and unpacking

4. **Custom Validation**: Using @field_validator decorators for custom validation logic

We need to install the following libraries:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. pydantic: pip install pydantic
4. pydantic[email]: pip install pydantic[email] (for EmailStr)

To run the application:
uvicorn Day_10.main:app --reload

### API Endpoints:
- `POST /users/`: Create a new user with validation

- `POST /users/dict/`: Create a new user using model_dump for dictionary conversion

### Files:
- **main.py**: Contains the FastAPI application code demonstrating Pydantic models, field validation, custom validators, and user creation endpoints.

---
# Day-11
## FastAPI with Redis (Folder: Day_11)

Redis (Remote Dictionary Server) is a key-value store that provides a persistent, in-memory data structure. It is often used for caching, session management, and distributed locking. It is a NoSQL Database with default port 6379.

This application demonstrates how to integrate Redis with FastAPI for caching API responses. It fetches data from an external API and caches it in Redis to improve performance on subsequent requests.

We need to install the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. redis: `pip install redis`
4. httpx: `pip install httpx`
5. python-dotenv: `pip install python-dotenv`

### Setting up Redis:
Users can access Redis using any of the following methods:

- **Local Installation**: Install Redis on your local machine

- **Docker**: Run Redis in a Docker container: docker run -d -p 6379:6379 redis

- **Online Services**: Use cloud Redis services like Redis Labs, AWS ElastiCache, etc.

Configure the REDIS_URL in a .env file if using a custom Redis instance.

To run the application:
uvicorn Day_11.main:app --reload

### API Endpoints:
- `GET /users`: Fetches user data from an external API and caches it in Redis for faster access.

### Files:
- **main.py**: Contains the FastAPI application code with Redis integration, caching logic, and external API calls.

---
# Day-12

## Real Time Chat Room with FastAPI and WebSockets (Folder: Day_12)

A simple real-time chat demo using FastAPI and WebSockets. The app serves a minimal HTML client at `/` and exposes a WebSocket endpoint at `/ws/{client_id}` to broadcast messages between connected clients.

Features:
- Embedded HTML chat UI served by the FastAPI app
- `ConnectionManager` to track active WebSocket connections
- Personal responses, broadcast messages, and join/leave notifications
- Graceful handling of disconnected clients (removes closed sockets)

Dependencies:
- `fastapi`
- `uvicorn`
- `websockets`

How to run:
1. Open a terminal in the project root or `Day_12` folder.
2. Run the server:

```bash
cd Day_12
uvicorn main:app --reload
```

3. Open `http://localhost:8000` in multiple browser tabs to test real-time chat (each tab gets a unique client id).

Files:
- `main.py`: WebSocket server, `ConnectionManager`, and embedded HTML client UI.

Notes:
- If you see errors about sending on closed websockets, ensure the server has been updated to remove closed connections before broadcasting.
- For production use, run behind a proper ASGI server, enable TLS (`wss://`) for WebSocket endpoints, and consider authentication.

---
# Day-13

## SQL Injection with FastAPI (Educational Purposes Only) (Folder: Day_13)

This application demonstrates the dangers of SQL injection vulnerabilities and how to prevent them using parameterized queries. It includes user registration and sign-in endpoints with SQLite database integration.

**WARNING: This code is for educational purposes only. Never use vulnerable SQL queries in production applications.**

We need to install the following libraries:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. sqlalchemy: pip install sqlalchemy
4. python-dotenv: pip install python-dotenv

Configure the SQLite_Database_URL in a .env file (e.g., SQLite_Database_URL=sqlite:///./test.db).

To run the application:
uvicorn Day_13.main:app --reload

### API Endpoints:
- POST /register/: Register a new user
- POST /signin/: Sign in with username and password

### Security Demonstration:
The code shows both vulnerable (commented out) and secure SQL query implementations. The vulnerable version concatenates user input directly into the SQL string, while the secure version uses parameterized queries to prevent SQL injection attacks.

### Files:
main.py: Contains the FastAPI application code demonstrating user registration, sign-in, and SQL injection prevention techniques.

---
# Day-14

## FastAPI with Pytest (Python Unit Testing) (Folder: Day_14)

This application demonstrates how to write and run unit tests for a FastAPI application using Pytest. It includes a simple Todo application with CRUD operations and comprehensive test coverage.

We need to install the following libraries:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. pytest: pip install pytest
4. httpx: pip install httpx (for testing async endpoints)

To run the application:
uvicorn Day_14.main:app --reload

To run the tests:
pytest Day_14/test_main.py

### API Endpoints:
- GET /: Retrieve all todos
- GET /{todo_id}: Retrieve a specific todo by ID
- POST /: Create a new todo
- PUT /{todo_id}: Update an existing todo
- DELETE /{todo_id}: Delete a todo

### Todo Object Structure:
```json
{
  "name": "Buy groceries",
  "completed": false
}
```

### Testing Features:
- Unit tests for all CRUD operations
- Tests for successful operations and error cases (404 for non-existent todos)
- Use of TestClient for simulating HTTP requests
- Async testing support with httpx

### Files:
- main.py: Contains the FastAPI application code with Todo CRUD operations
- test_main.py: Contains comprehensive unit tests for the Todo API endpoints
