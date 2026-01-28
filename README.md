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

---
# Day-15

## FastAPI with Async Operations and Background Tasks (CQRS Architecture) (Folder: Day_15)

This application demonstrates advanced FastAPI features including asynchronous database operations with SQLModel, service layer architecture, background tasks, and application lifespan management. It provides a simple item management API with create and read operations.

We need to install the following libraries:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn[standard]
3. sqlmodel: pip install sqlmodel
4. sqlalchemy[asyncio]: pip install sqlalchemy[asyncio]
5. python-dotenv: pip install python-dotenv

Configure the DAY_15_DATABASE_URL in a .env file (e.g., DAY_15_DATABASE_URL=sqlite+aiosqlite:///./test.db).

To run the application:
uvicorn Day_15.main:app --reload

### API Endpoints:
- GET /items/: Retrieve all items
- GET /items/{item_id}: Retrieve a specific item by ID
- POST /items/: Create a new item (triggers background logging task)

### Item Object Structure:
```json
{
  "name": "Sample Item",
  "description": "A sample item description"
}
```

### Features:
- **Async Database Operations**: Uses SQLAlchemy's async engine for non-blocking database interactions
- **Service Layer**: Separates business logic into a dedicated service class
- **Background Tasks**: Demonstrates background task execution for logging operations after item creation
- **Lifespan Management**: Uses FastAPI's lifespan context manager for database initialization and cleanup
- **SQLModel Integration**: Leverages SQLModel for type-safe database models and Pydantic validation

### Files:
main.py: Contains the FastAPI application code with async database operations, service layer, and background tasks

---
# Day-16

## FastAPI Rate Limiting with Middleware (Folder: Day_16)

This application demonstrates how to implement middleware in FastAPI for request logging, rate limiting, and custom headers. It includes two examples: a simple middleware using the @app.middleware decorator and an advanced middleware class with rate limiting functionality.

We need to install the following libraries:
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn

To run the simple middleware example:
uvicorn Day_16.main:app --reload

To run the advanced middleware with rate limiting:
uvicorn Day_16.rate_limiter:app --reload

### API Endpoints:
- GET /: Returns a welcome message (both examples)

### Middleware Features:
- **Request ID Logging**: Generates and logs a unique request ID for each request, adds it to response headers
- **Rate Limiting**: Limits requests to 1 per second per IP address, returns 429 status for exceeded limits
- **Request Logging**: Logs incoming requests with path, IP, and timestamp
- **Processing Time Tracking**: Measures and logs request processing time
- **Custom Headers**: Adds processing time to response headers

### Middleware Types Demonstrated:
- **Function-based Middleware**: Using @app.middleware("http") decorator
- **Class-based Middleware**: Extending BaseHTTPMiddleware for more complex logic

### Files:
- main.py: Contains the FastAPI application with simple function-based middleware for request ID logging
- rate_limiter.py: Contains the FastAPI application with advanced class-based middleware implementing rate limiting and detailed logging

---
# Day-17

## FastAPI with Docker Containerization (Folder: Day_17)

This application demonstrates how to containerize a FastAPI application using Docker. It includes a simple user management API with SQLite database integration, background tasks, and dependency injection. The app is packaged in a Docker container for easy deployment and portability.

We need to install the following libraries (included in requirements.txt):
1. fastapi: pip install fastapi
2. uvicorn: pip install uvicorn
3. sqlalchemy: pip install sqlalchemy

### Running Locally:
```bash
cd Day_17
uvicorn app.main:app --reload
```
Application runs on: `http://localhost:8000`

### Docker Deployment:

#### Build the Docker Image:
```bash
cd Day_17
docker build -t fastapi-docker .
```

#### Run the Docker Container:
```bash
docker run -d --name fastapi-docker-container -p 80:80 fastapi-docker
```
The application will be accessible at `http://localhost:80`

#### Stop and Remove Container (if needed):
```bash
docker stop fastapi-docker-container
docker rm fastapi-docker-container
```

### API Endpoints:
- GET /user/: Retrieve all users from the database
- POST /user/: Create a new user (accepts 'name' parameter, triggers background logging task)

### User Object Structure:
```json
{
  "id": 1,
  "name": "John Doe"
}
```

### Features:
- **SQLite Database**: Local database for user storage with SQLAlchemy ORM
- **Background Tasks**: Asynchronous task execution for logging user creation
- **Dependency Injection**: Database session management with FastAPI dependencies
- **Docker Containerization**: Complete container setup with Python 3.11 base image
- **Port Mapping**: Container runs on port 80, mapped to host port 80

### Files:
- **Dockerfile**: Docker configuration for building the container image
- **requirements.txt**: Python dependencies for the application
- **app/main.py**: FastAPI application code with user management endpoints and database models

### Docker Configuration:
- **Base Image**: Python 3.11
- **Working Directory**: /app
- **Exposed Port**: 80
- **Command**: uvicorn app.main:app --host 0.0.0.0 --port 80

---
# Day-18

## JWT Authentication for FastAPI and React (Folder: Day_18)

This application demonstrates a complete full-stack authentication system using JWT (JSON Web Tokens) with FastAPI backend and React frontend. It includes user registration, login, token-based authentication, and protected routes. The backend uses SQLAlchemy for database management and bcrypt for password hashing, while the frontend uses React Router for navigation and localStorage for token management.

We need to install the following libraries:

### Backend (FastAPI):
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. sqlalchemy: `pip install sqlalchemy`
4. python-jose: `pip install python-jose[cryptography]` (for JWT encoding/decoding)
5. passlib[bcrypt]: `pip install passlib[bcrypt]` (for password hashing)
6. python-dotenv: `pip install python-dotenv`
7. python-multipart: `pip install python-multipart` (for form data)

### Frontend (React):
1. react: Built with Create React App
2. react-router-dom: `npm install react-router-dom` (for routing)

### Database:
SQLite - A lightweight, file-based database (database.db)

### Environment Setup:
Create a `.env` file in the backend directory with:
```
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
```

### Running the Application:

**Backend (FastAPI Server):**
```bash
cd Day_18/backend
uvicorn main:app --reload
```
Backend runs on: `http://localhost:8000`

**Frontend (React App):**
```bash
cd Day_18/frontend/auth-app
npm install
npm start
```
Frontend runs on: `http://localhost:3000`

### API Endpoints:
- `POST /register`: Register a new user (accepts username and password)
- `POST /token`: Login and get access token (OAuth2 form data)
- `GET /verify_token/{token}`: Verify if a token is valid

### User Registration Object:
```json
{
  "username": "johndoe",
  "password": "securepassword"
}
```

### Login Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Backend Files:
- **main.py**: FastAPI application with JWT authentication, CORS middleware, user registration, login, and token verification endpoints
- **models.py**: SQLAlchemy User model with username and hashed password fields
- **database.py**: SQLite database connection setup using SQLAlchemy

### Frontend Files:
- **App.js**: Main React component with routing setup for Login and Protected pages
- **Login.js**: Login form component that handles user authentication and token storage
- **Protected.js**: Protected page component that verifies JWT token on load and redirects if invalid

### Features:
- **User Registration**: Secure user registration with password hashing using bcrypt
- **JWT Authentication**: Token-based authentication with configurable expiration (30 minutes)
- **Protected Routes**: Frontend routes that require valid JWT tokens
- **Token Verification**: Backend endpoint to verify token validity
- **CORS Support**: Cross-origin resource sharing enabled for frontend-backend communication
- **OAuth2 Compatible**: Login endpoint follows OAuth2 password flow standards
- **Local Storage**: Frontend stores JWT tokens in browser localStorage
- **Automatic Redirects**: Invalid tokens automatically redirect users to login page

### Security Features:
- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Tokens**: Stateless authentication with signed tokens
- **Token Expiration**: Access tokens expire after 30 minutes
- **CORS Protection**: Configured origins for secure cross-origin requests

### Authentication Flow:
1. User registers with username and password
2. Password is hashed and stored in database
3. User logs in with credentials
4. Backend validates credentials and returns JWT token
5. Frontend stores token in localStorage
6. Protected routes verify token with backend before rendering
7. Invalid/expired tokens redirect to login page

### Notes:
- The application uses SQLite for simplicity, but can be easily adapted to PostgreSQL, MySQL, etc.
- JWT secret key should be kept secure and not committed to version control
- For production, consider using HTTPS and more secure token storage mechanisms
- Token refresh mechanism can be added for better user experience

---
# Day-19

## JWT Authentication and Todo Management with FastAPI and Vue.js (Folder: Day_19)

This application demonstrates a complete full-stack Todo management system with JWT authentication using FastAPI backend and Vue.js frontend. It includes user registration, login, token-based authentication, and CRUD operations for todos. The backend uses SQLAlchemy for database management and bcrypt for password hashing, while the frontend uses Vue Router for navigation and localStorage for token management.

We need to install the following libraries:

### Backend (FastAPI):
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. sqlalchemy: `pip install sqlalchemy`
4. python-jose: `pip install python-jose[cryptography]` (for JWT encoding/decoding)
5. passlib[bcrypt]: `pip install passlib[bcrypt]` (for password hashing)
6. python-dotenv: `pip install python-dotenv`
7. python-multipart: `pip install python-multipart` (for form data)

### Frontend (Vue.js):
1. vue: Built with Vue CLI
2. vue-router: `npm install vue-router` (for routing)
3. axios: `npm install axios` (for HTTP requests)

### Database:
SQLite - A lightweight, file-based database (test_19.db)

### Environment Setup:
Create a `.env` file in the fastapi directory with:
```
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
DAY_19-DATABASE_URL=sqlite:///./test_19.db
```

### Running the Application:

**Backend (FastAPI Server):**
```bash
cd Day_19/fastapi
uvicorn main:app --reload
```
Backend runs on: `http://localhost:8000`

**Frontend (Vue.js App):**
```bash
cd Day_19/vue/vue-todo-app
npm install
npm run serve
```
Frontend runs on: `http://localhost:8080`

### API Endpoints:
- `POST /register`: Register a new user and return access token
- `POST /token`: Login and get access token (OAuth2 form data)
- `GET /users/me`: Get current user information (requires authentication)
- `POST /todos/`: Create a new todo (requires authentication)
- `DELETE /todos/{todo_id}`: Delete a todo by ID (requires authentication)

### User Registration Object:
```json
{
  "username": "johndoe",
  "password": "securepassword"
}
```

### Login Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Todo Create Object:
```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs"
}
```

### Backend Files:
- **main.py**: FastAPI application with JWT authentication, CORS middleware, user management, and todo CRUD operations

### Frontend Files:
- **App.vue**: Main Vue component with router-view setup
- **main.js**: Vue application entry point with router configuration
- **router/index.js**: Vue Router configuration with routes for registration, login, and todos
- **components/UserRegister.vue**: User registration form component
- **components/UserLogin.vue**: User login form component with token storage
- **components/TodoList.vue**: Todo management component with create and delete functionality
- **assets/custom.css**: Custom styling for the application

### Features:
- **User Registration**: Secure user registration with password hashing using bcrypt
- **JWT Authentication**: Token-based authentication with configurable expiration (60 minutes)
- **Protected Routes**: Frontend routes that require valid JWT tokens
- **Todo Management**: Full CRUD operations for todos (Create, Read, Delete)
- **CORS Support**: Cross-origin resource sharing enabled for frontend-backend communication
- **OAuth2 Compatible**: Login endpoint follows OAuth2 password flow standards
- **Local Storage**: Frontend stores JWT tokens in browser localStorage
- **Vue Router**: Client-side routing for different application views

### Security Features:
- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Tokens**: Stateless authentication with signed tokens
- **Token Expiration**: Access tokens expire after 60 minutes
- **CORS Protection**: Configured origins for secure cross-origin requests

### Authentication Flow:
1. User registers with username and password
2. Password is hashed and stored in database
3. User logs in with credentials
4. Backend validates credentials and returns JWT token
5. Frontend stores token in localStorage
6. Protected routes include token in Authorization header
7. Invalid/expired tokens prevent access to protected resources

### Todo Management Flow:
1. Authenticated user creates new todos
2. Todos are stored in database with user ownership
3. User can view their todos
4. User can delete their todos
5. All operations require valid JWT authentication

### Notes:
- The application uses SQLite for simplicity, but can be easily adapted to PostgreSQL, MySQL, etc.
- JWT secret key should be kept secure and not committed to version control
- For production, consider using HTTPS and more secure token storage mechanisms
- Token refresh mechanism can be added for better user experience
- The frontend uses Vue 2 with Vue Router for navigation

---
# Day-20

## Fitness Tracker with FastAPI and Next.js (Folder: Day_20)

This application demonstrates a complete full-stack fitness tracking system with JWT authentication using FastAPI backend and Next.js frontend. It includes user registration, login, token-based authentication, and CRUD operations for workouts and routines. The backend uses SQLAlchemy for database management and bcrypt for password hashing, while the frontend uses Next.js with React components for navigation and localStorage for token management.

We need to install the following libraries:

### Backend (FastAPI):
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. sqlalchemy: `pip install sqlalchemy`
4. python-jose: `pip install python-jose[cryptography]` (for JWT encoding/decoding)
5. passlib[bcrypt]: `pip install passlib[bcrypt]` (for password hashing)
6. python-dotenv: `pip install python-dotenv`
7. python-multipart: `pip install python-multipart` (for form data)

### Frontend (Next.js):
1. next: Built with Next.js
2. react: React components
3. axios: `npm install axios` (for HTTP requests)

### Database:
SQLite - A lightweight, file-based database (fitness.db)

### Environment Setup:
Create a `.env` file in the fastapi directory with:
```
DAY_20_AUTH_SECRET_KEY=your-secret-key-here
DAY_20_AUTH_ALGORITHM=HS256
```

### Running the Application:

**Backend (FastAPI Server):**
```bash
cd Day_20/fastapi
uvicorn api.main:app --reload
```
Backend runs on: `http://localhost:8000`

**Frontend (Next.js App):**
```bash
cd Day_20/nextjs
npm install
npm run dev
```
Frontend runs on: `http://localhost:3000`

### API Endpoints:
- `POST /auth/register`: Register a new user and return access token
- `POST /auth/token`: Login and get access token (OAuth2 form data)
- `GET /workouts`: Get all workouts for the authenticated user
- `GET /workouts/{workout_id}`: Get a specific workout by ID
- `POST /workouts`: Create a new workout (requires authentication)
- `DELETE /workouts/{workout_id}`: Delete a workout by ID (requires authentication)
- `GET /routines`: Get all routines for the authenticated user
- `POST /routines`: Create a new routine with selected workouts (requires authentication)

### User Registration Object:
```json
{
  "username": "johndoe",
  "password": "securepassword"
}
```

### Login Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Workout Create Object:
```json
{
  "name": "Push-ups",
  "description": "Upper body strength exercise"
}
```

### Routine Create Object:
```json
{
  "name": "Morning Workout",
  "description": "Daily routine for fitness",
  "workouts": [1, 2, 3]
}
```

### Backend Files:
- **api/main.py**: FastAPI application with JWT authentication, CORS middleware, user management, and workout/routine CRUD operations
- **api/models.py**: SQLAlchemy models for User, Workout, and Routine tables with relationships
- **api/database.py**: SQLite database connection setup using SQLAlchemy
- **api/deps.py**: Authentication dependencies including JWT token validation and database session management
- **api/routers/auth.py**: Authentication router with registration and login endpoints
- **api/routers/workouts.py**: Workouts router with CRUD operations
- **api/routers/routines.py**: Routines router with CRUD operations

### Frontend Files:
- **src/app/page.js**: Main Next.js page with workout and routine management using React hooks
- **src/app/login/page.js**: Login page component for user authentication
- **src/app/components/ProtectedRoute.js**: Protected route component that verifies JWT tokens
- **src/app/context/AuthContext.js**: React context for managing authentication state
- **src/app/layout.js**: Root layout component with global styles
- **src/app/globals.css**: Global CSS styles for the application

### Features:
- **User Registration**: Secure user registration with password hashing using bcrypt
- **JWT Authentication**: Token-based authentication with configurable expiration
- **Protected Routes**: Frontend routes that require valid JWT tokens
- **Workout Management**: Full CRUD operations for workouts (Create, Read, Update, Delete)
- **Routine Management**: Create routines by selecting multiple workouts
- **CORS Support**: Cross-origin resource sharing enabled for frontend-backend communication
- **OAuth2 Compatible**: Login endpoint follows OAuth2 password flow standards
- **Local Storage**: Frontend stores JWT tokens in browser localStorage
- **Next.js Routing**: Client-side routing for different application views

### Security Features:
- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Tokens**: Stateless authentication with signed tokens
- **Token Expiration**: Access tokens expire after authentication
- **CORS Protection**: Configured origins for secure cross-origin requests

### Authentication Flow:
1. User registers with username and password
2. Password is hashed and stored in database
3. User logs in with credentials
4. Backend validates credentials and returns JWT token
5. Frontend stores token in localStorage
6. Protected routes include token in Authorization header
7. Invalid/expired tokens prevent access to protected resources

### Workout and Routine Management Flow:
1. Authenticated user creates workouts with name and description
2. Workouts are stored in database with user ownership
3. User can view all their workouts
4. User can create routines by selecting multiple workouts
5. Routines display associated workouts
6. All operations require valid JWT authentication

### Notes:
- The application uses SQLite for simplicity, but can be easily adapted to PostgreSQL, MySQL, etc.
- JWT secret key should be kept secure and not committed to version control
- For production, consider using HTTPS and more secure token storage mechanisms
- Token refresh mechanism can be added for better user experience
- The frontend uses Next.js 13 with App Router for modern React development

---
# Day-21

## SQLModel: Modern ORM for FastAPI (Folder: Day_21)

This application demonstrates SQLModel, a modern ORM that combines the power of SQLAlchemy and Pydantic. SQLModel provides type-safe database models with automatic data validation, making it perfect for FastAPI applications. It supports relationships, CRUD operations, and seamless integration with FastAPI's dependency injection system.

We need to install the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. sqlmodel: `pip install sqlmodel`

### Database:
SQLite - A lightweight, file-based database (orm.db)

To run the application:
```bash
cd Day_21
python main.py
```

### Features Demonstrated:
- **SQLModel Tables**: Defining database models with automatic table creation
- **Relationships**: One-to-many relationships between Author and Book models
- **CRUD Operations**: Create, Read, Update, Delete operations using SQLModel sessions
- **Joins**: Performing joins to fetch related data
- **Type Safety**: Full type hints and Pydantic validation

### Models:
- **Author**: Represents book authors with id, name, and email fields
- **Book**: Represents books with id, title, content, and foreign key to author

### Operations Demonstrated:
1. **Create**: Adding authors and books to the database
2. **Read**: Querying books and authors with various filters
3. **Update**: Modifying existing book records
4. **Delete**: Removing books from the database
5. **Joins**: Fetching books with their associated authors

### Files:
- **main.py**: Contains the SQLModel application code demonstrating ORM operations, model definitions, and database interactions.

### Key Concepts:
- **SQLModel Metadata**: Using `SQLModel.metadata.create_all()` for table creation
- **Session Management**: Using `Session` context manager for database operations
- **Query Building**: Using `select()` statements with filters and joins
- **Relationship Navigation**: Accessing related objects through relationship attributes

### Notes:
- SQLModel provides a clean, type-safe way to work with databases in Python
- It automatically generates Pydantic models from SQLAlchemy models
- Perfect for FastAPI applications requiring database integration
- Supports all major databases through SQLAlchemy

---
# Day-22

## Dependency Injection in FastAPI (Folder: Day_22)

This application demonstrates the powerful dependency injection system in FastAPI, showcasing how to create reusable service classes and inject them into your API endpoints. Dependency injection promotes clean architecture, testability, and separation of concerns by allowing services to be easily swapped or mocked.

We need to install the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`

To run the application:
```bash
cd Day_22
uvicorn main:app --reload
```
Application runs on: `http://localhost:8000`

### Features Demonstrated:
- **Service Classes**: Creating reusable service classes (AuthService, EmailService, Logger)
- **Dependency Injection**: Using FastAPI's `Depends` to inject services into endpoints
- **Annotated Dependencies**: Using `typing.Annotated` for cleaner dependency declarations
- **Authentication Service**: Token-based authentication with service injection
- **Logging Service**: Centralized logging functionality
- **Email Service**: Mock email sending service for notifications

### Services Demonstrated:
- **AuthService**: Handles token authentication and raises HTTP exceptions for invalid tokens
- **EmailService**: Simulates email sending (prints to console for demonstration)
- **Logger**: Provides centralized logging functionality for application events

### API Endpoints:
- `GET /log/{message}`: Logs a message using the injected Logger service and returns the message
- `GET /secure-data/?token={token}`: Returns secure data only if a valid token is provided (uses AuthService)

### Endpoint Examples:
```bash
# Log a message
GET /log/Hello%20World

# Access secure data with valid token
GET /secure-data/?token=valid-token

# Access secure data with invalid token (returns 401)
GET /secure-data/?token=invalid-token
```

### Files:
- **main.py**: Contains the main FastAPI application with Logger service and logging endpoint
- **auth_service.py**: Contains the AuthService class and secure data endpoint with authentication
- **email.py**: Contains the EmailService class for email functionality (demonstration purposes)

### Key Concepts:
- **Depends Function**: Using `Depends(get_service)` to inject service instances
- **Annotated Dependencies**: Cleaner syntax with `Annotated[ServiceType, Depends(get_service)]`
- **Service Layer Pattern**: Separating business logic into dedicated service classes
- **HTTP Exceptions**: Raising appropriate HTTP status codes from service methods
- **Singleton Services**: Services created once per request by default

### Dependency Injection Benefits:
- **Testability**: Easy to mock services for unit testing
- **Modularity**: Services can be developed and tested independently
- **Reusability**: Same service can be injected into multiple endpoints
- **Clean Architecture**: Separation of concerns between routing and business logic

### Notes:
- FastAPI's dependency injection is powerful and flexible
- Services are instantiated per request by default
- Use `Annotated` for cleaner, more readable dependency declarations
- Services can have their own dependencies, creating a dependency graph
- Perfect for implementing service layer architecture in FastAPI applications

---
# Day-23

## GraphQL API with FastAPI and Strawberry (Folder: Day_23)

This application demonstrates how to build a GraphQL API using FastAPI and Strawberry. GraphQL provides a flexible query language for APIs, allowing clients to request exactly the data they need. The application includes user and post management with relationships, showcasing GraphQL queries and mutations with SQLModel for database operations.

We need to install the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. strawberry-graphql: `pip install strawberry-graphql[fastapi]`
4. sqlmodel: `pip install sqlmodel`
5. python-dotenv: `pip install python-dotenv`

Configure the DAY_23_DATABASE_URL in a .env file (e.g., DAY_23_DATABASE_URL=sqlite:///./test_23.db).

To run the application:
```bash
cd Day_23
uvicorn main:app --reload
```
Application runs on: `http://localhost:8000`

GraphQL playground is available at: `http://localhost:8000/graphql`

### Features Demonstrated:
- **GraphQL Schema**: Defining types, queries, and mutations with Strawberry
- **SQLModel Integration**: Using SQLModel for database models with relationships
- **GraphQL Queries**: Fetching users and posts with flexible data selection
- **GraphQL Mutations**: Creating new users and posts
- **FastAPI Integration**: Combining GraphQL with FastAPI's features
- **Database Relationships**: One-to-many relationships between users and posts

### GraphQL Schema:
- **UserType**: Represents users with id, name, email, and associated posts
- **PostType**: Represents posts with id, title, and content
- **Query**: get_user(id) and get_post(id) operations
- **Mutation**: create_user(name, email) and create_post(title, content, author_id) operations

### GraphQL Queries Examples:

**Get a user with their posts:**
```graphql
query {
  getUser(id: 1) {
    id
    name
    email
    posts {
      id
      title
      content
    }
  }
}
```

**Get a specific post:**
```graphql
query {
  getPost(id: 1) {
    id
    title
    content
  }
}
```

### GraphQL Mutations Examples:

**Create a new user:**
```graphql
mutation {
  createUser(name: "John Doe", email: "john@example.com") {
    id
    name
    email
  }
}
```

**Create a new post:**
```graphql
mutation {
  createPost(title: "My First Post", content: "This is the content", authorId: 1) {
    id
    title
    content
  }
}
```

### Database Models:
- **User**: id, name, email, posts (relationship)
- **Post**: id, title, content, author_id (foreign key)

### Files:
- **main.py**: Contains the FastAPI application with GraphQL schema, SQLModel models, and GraphQL router integration

### Key Concepts:
- **Strawberry Types**: Using @strawberry.type for GraphQL type definitions
- **GraphQL Fields**: Using @strawberry.field for query and mutation definitions
- **Schema Creation**: Combining queries and mutations into a GraphQL schema
- **FastAPI Router**: Integrating GraphQL with FastAPI using GraphQLRouter
- **SQLModel Sessions**: Using database sessions for data operations

### GraphQL Benefits:
- **Flexible Queries**: Clients can request exactly the data they need
- **Single Endpoint**: All operations go through one GraphQL endpoint
- **Type Safety**: Strongly typed schema prevents invalid queries
- **Introspection**: Built-in schema exploration capabilities
- **Real-time Updates**: Can be extended with subscriptions for real-time data

### Notes:
- GraphQL provides more flexibility than REST APIs for complex data requirements
- Strawberry offers excellent FastAPI integration with type hints
- The GraphQL playground provides an interactive way to test queries and mutations
- SQLModel provides seamless integration with GraphQL resolvers
- Perfect for applications requiring complex, nested data relationships

---
# Day-24

## Poetry: Dependency Management for FastAPI (Folder: Day_24)

This application demonstrates how to use Poetry for dependency management in a FastAPI project. Poetry is a modern Python dependency management tool that simplifies package installation, version management, and project configuration. It uses a single `pyproject.toml` file to manage all dependencies and project metadata, making workflows cleaner and more predictable.

Poetry helps avoid version conflicts within dependencies, unlike traditional `requirements.txt` files, and removes manual work from dependency management in Python projects.

### Key Features of Poetry:
- **Single Configuration File**: Uses `pyproject.toml` for all project configuration
- **Dependency Resolution**: Automatically resolves and manages package versions
- **Virtual Environment Management**: Creates and manages isolated environments
- **Build System**: Handles package building and distribution
- **Lock File**: `poetry.lock` ensures reproducible installations

### Installation:
```bash
pip install poetry
```

### Commands Used Today:

**Create a new Poetry project:**
```bash
poetry new fastapi-demo
cd fastapi-demo
```

**Add dependencies:**
```bash
poetry add fastapi uvicorn
```
This automatically installs FastAPI and Uvicorn, adds them to `pyproject.toml`, and updates `poetry.lock`.

**Install dependencies:**
```bash
poetry install
```
Installs all dependencies listed in `pyproject.toml` and `poetry.lock`.

**Run the application:**
```bash
poetry run uvicorn src.fastapi_demo.main:app --reload
```
Runs the FastAPI application using Poetry's virtual environment.

**Update dependencies:**
```bash
poetry update
```
Updates all dependencies to their latest compatible versions.

**Build for distribution:**
```bash
poetry build
```
Creates distribution packages in the `/dist` folder for production deployment.

### Project Structure:
The Poetry project follows a standard structure:
```
fastapi-demo/
├── pyproject.toml          # Project configuration and dependencies
├── poetry.lock             # Lock file for reproducible installs
├── README.md               # Project documentation
├── src/
│   └── fastapi_demo/       # Source code package
│       ├── __init__.py
│       └── main.py         # FastAPI application
└── tests/                  # Test directory
    └── __init__.py
```

### Running the Application:
```bash
cd Day_24/fastapi-demo
poetry run uvicorn src.fastapi_demo.main:app --reload
```
Application runs on: `http://localhost:8000`

### API Endpoints:
- `GET /`: Returns a welcome message with "Hello World"

### Files:
- **pyproject.toml**: Poetry configuration file with project metadata and dependencies
- **poetry.lock**: Lock file ensuring consistent dependency versions
- **src/fastapi_demo/main.py**: Simple FastAPI application with a root endpoint
- **README.md**: Project documentation

### Key Concepts:
- **pyproject.toml**: Modern Python project configuration standard (PEP 621)
- **Poetry Lock File**: Ensures all environments have identical dependency versions
- **Source Layout**: Uses `src/` layout for better package structure
- **Virtual Environments**: Poetry automatically manages isolated environments
- **Dependency Groups**: Can define different dependency sets for development, testing, etc.

### Poetry Benefits:
- **Reproducible Builds**: Lock file ensures consistent environments
- **Version Resolution**: Automatically handles dependency conflicts
- **Clean Workflow**: Single tool for all dependency management tasks
- **Modern Standards**: Uses current Python packaging standards
- **IDE Integration**: Works well with modern Python development tools

### Notes:
- Poetry creates virtual environments automatically in a `.venv` folder
- The `src/` layout prevents import issues during development
- `poetry.lock` should be committed to version control for reproducible builds
- Poetry integrates well with CI/CD pipelines and containerization
- Perfect for professional Python projects requiring reliable dependency management

---
# Day-25

## OpenTelemetry with FastAPI (Folder: Day_25)

This application demonstrates OpenTelemetry integration with FastAPI for distributed tracing, metrics, and logging. OpenTelemetry is an open-source framework for tracking telemetry data to monitor application performance and identify failures in real-time.

We need to install the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. opentelemetry-distro: `pip install opentelemetry-distro`
4. opentelemetry-instrumentation-fastapi: `pip install opentelemetry-instrumentation-fastapi`

To run the application:
```bash
cd Day_25
opentelemetry-instrument --traces_exporter console --metrics_exporter console --logs_exporter console --service_name dice_server uvicorn main:app --reload
```
Application runs on: `http://localhost:8000`

### API Endpoints:
- `GET /rolldice`: Rolls 15 dice, distributes them into 3 lists of 5 each, and returns the results with OpenTelemetry tracing.

### Files:
- **main.py**: Contains the FastAPI application code with OpenTelemetry tracing for dice rolling.

---
# Day-26

## Employee Management System with Supabase (Folder: Day_26)

This application demonstrates how to build a full-stack employee management system using FastAPI with Supabase as the backend. Supabase provides PostgreSQL database, authentication, and file storage capabilities. The application includes user authentication with JWT tokens, CRUD operations for employee management, and image upload functionality with a beautiful web interface.

We need to install the following libraries:
1. fastapi: `pip install fastapi`
2. uvicorn: `pip install uvicorn`
3. supabase: `pip install supabase`
4. python-dotenv: `pip install python-dotenv`
5. pydantic[email]: `pip install pydantic[email]`
6. python-multipart: `pip install python-multipart`
7. pyjwt: `pip install pyjwt`

Configure the following environment variables in a .env file:
```env
DAY_26_SUPABASE_URL=your_supabase_project_url
DAY_26_SUPABASE_KEY=your_supabase_anon_key
DAY_26_SUPABASE_BUCKET=demo-bucket
DAY_26_SUPABASE_JWT_SECRET=your_jwt_secret
```

### Supabase Setup:

**1. Create the employees table:**
```sql
create table employees (
  id serial primary key,
  first_name text not null,
  last_name text not null,
  email text unique not null,
  salary numeric not null,
  image_url text,
  is_active boolean default true
);
```

**2. Configure Row Level Security (RLS):**
- Option A: Disable RLS on the employees table (easiest for development)
- Option B: Add RLS policy:
```sql
CREATE POLICY "Enable all access for employees"
ON employees
FOR ALL
TO public
USING (true)
WITH CHECK (true);
```

**3. Configure Storage Bucket:**
- Create a bucket named `demo-bucket`
- Set bucket to Public
- Add storage policy:
```sql
CREATE POLICY "Public Access"
ON storage.objects
FOR ALL
TO public
USING (bucket_id = 'demo-bucket')
WITH CHECK (bucket_id = 'demo-bucket');
```

To run the application:
```bash
cd Day_26
uvicorn employee_repo.main:app --reload
```
Application runs on: `http://localhost:8000`

### Features Demonstrated:
- **User Authentication**: Sign up, login, and logout with JWT tokens
- **Employee CRUD**: Create, read, update, and delete employee records
- **Image Upload**: Upload and store employee profile images in Supabase Storage
- **Soft Delete**: Mark employees as inactive instead of permanent deletion
- **Form Validation**: Pydantic models with email validation and salary constraints
- **Responsive UI**: Modern, gradient-themed web interface with proper styling
- **Session Management**: Cookie-based authentication with httponly cookies

### API Endpoints:

**Authentication Routes:**
- `GET /signup`: Display signup form
- `POST /signup`: Create new user account
- `GET /login`: Display login form
- `POST /login`: Authenticate user and create session
- `GET /logout`: Clear session and logout user

**Employee Management Routes:**
- `GET /`: List all active employees
- `GET /add`: Display add employee form
- `POST /add`: Create new employee with optional image
- `GET /edit/{employee_id}`: Display edit employee form
- `POST /edit/{employee_id}`: Update employee details
- `POST /delete/{employee_id}`: Soft delete employee (mark as inactive)

### Project Structure:
```
Day_26/
├── employee_repo/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── employee_routes.py    # Employee CRUD operations
│   │   └── auth_routes.py        # Authentication endpoints
│   ├── static/
│   │   └── style.css             # Application styling
│   ├── templates/
│   │   ├── index.html            # Employee list dashboard
│   │   ├── add_employee.html     # Add employee form
│   │   ├── edit_employee.html    # Edit employee form
│   │   ├── login.html            # Login page
│   │   └── signup.html           # Registration page
│   ├── __init__.py
│   ├── main.py                   # FastAPI application entry point
│   ├── database.py               # Supabase client configuration
│   ├── models.py                 # Pydantic models
│   ├── forms.py                  # Form handling decorator
│   └── auth.py                   # Authentication middleware
├── .env                          # Environment variables
└── requirements.txt              # Project dependencies
```

### Database Models:
- **Employee**: 
  - id (serial primary key)
  - first_name (text, required)
  - last_name (text, required)
  - email (text, unique, required)
  - salary (numeric, required, must be positive)
  - image_url (text, optional)
  - is_active (boolean, default true)

### Pydantic Models:
- **EmployeeBase**: Base model with first_name, last_name, email, and salary validation
- **EmployeeCreate**: Model for creating new employees
- **EmployeeUpdate**: Model for updating employees with is_active status field

### Key Concepts:
- **Supabase Client**: Using create_client for database and storage operations
- **JWT Authentication**: Token-based authentication with cookie storage
- **Form Data Handling**: Custom @as_form decorator for Pydantic models
- **File Upload**: Handling multipart form data with unique filename generation
- **Template Rendering**: Using Jinja2Templates for dynamic HTML pages
- **Static Files**: Serving CSS and other static assets
- **Environment Variables**: Secure configuration management with python-dotenv

### Supabase Features Used:
- **PostgreSQL Database**: Reliable relational database with SQL queries
- **Supabase Auth**: Built-in authentication with email/password
- **Supabase Storage**: File storage with public bucket access
- **Row Level Security**: Fine-grained access control policies
- **Real-time Capabilities**: Foundation for real-time updates (extendable)

### Security Features:
- **JWT Tokens**: Secure session management
- **HttpOnly Cookies**: Protection against XSS attacks
- **Password Hashing**: Handled by Supabase Auth
- **Email Validation**: Pydantic EmailStr validation
- **Input Sanitization**: Form validation with Pydantic models
- **Secure File Upload**: Unique filename generation to prevent conflicts

### UI Features:
- **Modern Design**: Purple gradient theme with clean aesthetics
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Interactive Tables**: Hover effects and action buttons
- **Form Validation**: Client-side and server-side validation
- **Status Indicators**: Visual Active/Inactive badges
- **Image Display**: Profile image thumbnails with fallback
- **Empty States**: Helpful messages when no data exists

### Image Upload Process:
1. Generate unique filename with timestamp and UUID
2. Read file content from multipart form data
3. Upload to Supabase Storage bucket
4. Store public URL in employee database record
5. Display image in employee list and edit forms

### Files:
- **main.py**: FastAPI application setup with route registration
- **database.py**: Supabase client initialization and configuration
- **models.py**: Pydantic models with validation for employees
- **forms.py**: Decorator for handling form data with Pydantic
- **auth.py**: Authentication middleware and JWT verification
- **employee_routes.py**: Employee CRUD endpoints with image handling
- **auth_routes.py**: User authentication endpoints (signup/login/logout)
- **style.css**: Complete styling for all pages and components
- **HTML templates**: Jinja2 templates for all pages

### Notes:
- Supabase provides a free tier perfect for development and small projects
- Images are stored with unique filenames to prevent overwriting
- Soft delete preserves data while hiding inactive employees
- JWT tokens are stored in httponly cookies for security
- The application uses PostgreSQL through Supabase's API
- Row Level Security policies can be customized for production use
- Form validation ensures data integrity at multiple levels
- The UI is fully responsive and works across all devices
- Perfect for learning full-stack development with modern tools

### Supabase Benefits:
- **Backend as a Service**: No server management required
- **PostgreSQL Database**: Powerful relational database with SQL
- **Built-in Auth**: User management and authentication included
- **File Storage**: S3-compatible object storage
- **Real-time**: WebSocket support for live updates
- **Auto-generated APIs**: REST and GraphQL APIs out of the box
- **Row Level Security**: Database-level access control
- **Dashboard**: Web interface for database and storage management

### Production Considerations:
- Enable and configure proper RLS policies for security
- Use service_role key for admin operations only
- Implement proper error handling and logging
- Add rate limiting for API endpoints
- Configure CORS properly for production domains
- Use environment-specific configuration
- Implement proper session timeout and refresh
- Add comprehensive input validation
- Configure backup and recovery strategies
- Monitor usage and performance metrics

---
# Day-27

## UV Python with FastAPI (Folder: Day_27)

This application demonstrates UV Python, a fast and modern Python package manager and project manager. UV is designed to be a drop-in replacement for pip and virtualenv, offering significantly faster performance and better dependency resolution. It automatically creates virtual environments and manages dependencies through a pyproject.toml file.

### Key Features of UV:
- **Fast Installation**: Significantly faster than pip for installing packages
- **Automatic Virtual Environments**: Creates and manages virtual environments automatically
- **Modern Standards**: Uses pyproject.toml for project configuration
- **Dependency Resolution**: Advanced dependency resolution to avoid conflicts
- **Drop-in Replacement**: Compatible with existing Python workflows

### Installation:
```bash
pip install uv
```

### Commands Used Today:

**Check Python versions:**
```bash
uv python list
```

**Install latest Python (if needed):**
```bash
uv python install
```

**Initialize a new project:**
```bash
uv init python-project
cd python-project
```

**Add dependencies:**
```bash
uv add fastapi uvicorn
```

**Remove dependencies:**
```bash
uv remove pytest
```

**Add extra dependencies:**
```bash
uv add fastapi --extra standard
```

**Run the application:**
```bash
uv run fastapi dev main.py
```

### Project Structure:
```
Day_27/python-project/
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Lock file for reproducible installs
├── README.md               # Project documentation
├── main.py                 # FastAPI application
├── .python-version         # Python version specification
└── .venv/                  # Virtual environment (auto-created)
```

### Running the Application:
```bash
cd Day_27/python-project
uv run fastapi dev main.py
```
Application runs on: `http://127.0.0.1:8000`

### API Endpoints:
- `GET /`: Returns a welcome message with "Hello World"

### Files:
- **main.py**: Simple FastAPI application with a root endpoint
- **pyproject.toml**: UV configuration file with project metadata and dependencies
- **uv.lock**: Lock file ensuring consistent dependency versions

### Key Concepts:
- **pyproject.toml**: Modern Python project configuration standard
- **UV Lock File**: Ensures reproducible installations across environments
- **Virtual Environment**: Automatically managed by UV
- **Fast Installation**: Optimized package installation and dependency resolution

### UV Benefits:
- **Performance**: Much faster than traditional pip installations
- **Simplicity**: Single tool for project and dependency management
- **Reproducibility**: Lock files ensure consistent environments
- **Modern Standards**: Follows current Python packaging best practices
- **Easy Migration**: Can work with existing Python projects

### Notes:
- UV automatically creates virtual environments in `.venv` folder
- The `uv.lock` file should be committed to version control
- UV integrates well with existing Python development workflows
- Perfect for modern Python projects requiring fast, reliable dependency management
- Can be used as a drop-in replacement for pip and virtualenv

---
# Day-28

## Pydantic: Data Validation and Settings Management (Folder: Day_28)

This application demonstrates Pydantic, a powerful data validation and settings management library for Python. Pydantic is the backbone of FastAPI and provides automatic data validation, serialization, and parsing. It ensures that your data is clean, correct, and exactly what you expect, handling errors gracefully without crashing your applications.

### Learning Goals:
1. What is Pydantic and why should we have it in our projects?
2. Live Example: How Pydantic saved a startup
3. Coding Examples so we can implement Pydantic in our projects

### What is Pydantic?

- **Data Validation Library**: At the core, it's all about making sure our data is clean, correct and exactly what we expect
- **Error Handling**: Handles the errors and exceptions without crashing our systems
- **Automatic Processing**: Does all these things behind the scenes so we don't need to add tons of code
- **Widely Used**: Very popular and comes automatically with FastAPI and SQLModel

### Key Features Demonstrated:

#### Field Validation:
- **String Length**: `min_length` and `max_length` constraints
- **Numeric Constraints**: `gt` (greater than), `lt` (less than) for age and height validation
- **Email Validation**: Built-in `EmailStr` for proper email format checking

#### Custom Validation:
- **Field Validators**: Using `@field_validator` decorator for custom validation logic
- **Regex Validation**: Username must contain only letters, numbers, and underscores
- **Uniqueness Check**: Ensuring usernames are unique across the application

### Installation:
```bash
pip install pydantic
pip install pydantic[email]  # For EmailStr support
```

### Code Example:

The application shows the evolution from manual class definition to Pydantic-powered validation:

**Before Pydantic (Manual Implementation):**
```python
class User():
    def __init__(self, name, age, height):
        self.name = name,
        self.age = age,
        self.height = height

    def __repr__(self):
        return f"User Attributes: Name: {self.name}, Age: {self.age}, Height: {self.height}"
```

**With Pydantic (Automatic Validation):**
```python
from pydantic import BaseModel, Field, EmailStr, field_validator
import re

usernames = ["kaustubh", "mukdam"]

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=18)
    height: int = Field(gt=40, lt=70)
    email: EmailStr
    username: str = Field(min_length=3, max_length=20)

    @field_validator("username")
    def validate_username(cls, value):
        if not re.match("^[a-zA-Z0-9_]+$", value):
            raise ValueError("Username must contain only letters, numbers, and underscores")
        if value in usernames:
            raise ValueError("Username must be unique")

        usernames.append(value)
        return value
```

### Running the Application:
```bash
cd Day_28
python main.py
```

### Validation Examples:

**Valid User:**
```python
user = User(name="Kaustubh Mukdam", age=21, height=60, email="test@example.com", username="KDM221005")
print(user)  # User(name='Kaustubh Mukdam', age=21, height=60, email='test@example.com', username='KDM221005')
```

**Invalid Examples:**
- `age=15` → ValidationError: Age must be greater than 18
- `height=30` → ValidationError: Height must be greater than 40
- `email="invalid-email"` → ValidationError: Invalid email format
- `username="user@123"` → ValidationError: Username must contain only letters, numbers, and underscores

### Files:
- **main.py**: Contains the Pydantic User model with comprehensive validation examples

### Key Concepts:
- **BaseModel**: Base class for all Pydantic models
- **Field**: Function for adding validation constraints to fields
- **EmailStr**: Special string type for email validation
- **@field_validator**: Decorator for custom field validation logic
- **Automatic Type Conversion**: Pydantic automatically converts types when possible
- **Detailed Error Messages**: Clear, actionable validation error messages

### Pydantic Benefits:
- **Type Safety**: Ensures data types match expectations
- **Automatic Validation**: No need to write manual validation code
- **Clear Error Messages**: Helpful error messages for debugging
- **Fast Performance**: Optimized validation with minimal overhead
- **IDE Support**: Excellent autocomplete and type hints
- **JSON Serialization**: Automatic conversion to/from JSON
- **FastAPI Integration**: Seamlessly works with FastAPI's request/response models

### Real-World Impact:
Pydantic has saved countless hours of development time and prevented numerous bugs by catching data validation issues early. Many startups and large companies rely on Pydantic for robust data handling in their APIs and applications.

### Notes:
- Pydantic v2 introduced significant performance improvements and new features
- It's the foundation of FastAPI's automatic request validation and response serialization
- Perfect for API development, configuration management, and any scenario requiring data validation
- Supports complex nested models, custom types, and advanced validation scenarios
- Essential tool for modern Python development, especially with FastAPI

---
# Day-29

## Video Streaming Platform with Supabase Storage (Folder: Day_29)

This application demonstrates building a full-stack video streaming platform using FastAPI and Supabase Storage. It showcases cloud storage integration, video streaming capabilities, file upload handling, and modern web development practices with server-side templating using Jinja2.

### Learning Goals:
1. How to integrate Supabase Storage with FastAPI
2. Implement video streaming with proper HTTP range requests
3. Handle file uploads with multipart form data
4. Build a modern, responsive UI with Jinja2 templates
5. Work with environment variables for secure configuration

### What is Supabase Storage?

- **Cloud Storage Solution**: S3-compatible object storage built on top of PostgreSQL
- **Public/Private Buckets**: Flexible access control for your files
- **REST API**: Easy integration with any programming language
- **CDN Integration**: Fast content delivery worldwide
- **File Management**: Upload, download, delete, and list files with simple API calls

### Key Features Demonstrated:

#### Backend Features:
- **Video Streaming**: Efficient video delivery using HTTP streaming with range requests
- **File Upload**: Handle multipart form data for video file uploads
- **Storage Integration**: Direct integration with Supabase storage buckets
- **Error Handling**: Proper HTTP exception handling for missing videos
- **Template Rendering**: Server-side rendering with Jinja2 for dynamic HTML

#### Frontend Features:
- **Responsive Video Grid**: Modern card-based layout for video browsing
- **Video Player**: Native HTML5 video player with full controls
- **Drag & Drop Upload**: Intuitive file upload with drag-and-drop support
- **Dark Theme UI**: Netflix-inspired modern dark interface
- **Keyboard Shortcuts**: Enhanced video player controls (Space, Arrow keys, F for fullscreen)
- **Upload Progress**: Visual feedback during file upload process

### Installation:

**Install dependencies:**
```bash
pip install fastapi uvicorn python-dotenv supabase httpx jinja2 python-multipart
```

Or using UV:
```bash
uv add fastapi uvicorn python-dotenv supabase httpx jinja2 python-multipart
```

### Environment Setup:

Create a `.env` file in the Day_29 directory:
```env
DAY_29_SUPABASE_URL=your_supabase_project_url
DAY_29_SUPABASE_ANON_KEY=your_supabase_anon_key
DAY_29_SUPABASE_BUCKET=your_bucket_name
```

### Supabase Setup:

1. **Create a Supabase Project**: Sign up at [supabase.com](https://supabase.com)
2. **Create a Storage Bucket**:
   - Navigate to Storage in your project
   - Create a new bucket (e.g., "videos")
   - Set bucket to public for video streaming
3. **Get Credentials**:
   - Project URL: Found in Project Settings → API
   - Anon Key: Found in Project Settings → API
   - Bucket Name: The name you gave your storage bucket

### Project Structure:
```
Day_29/
├── main.py                 # FastAPI application with all endpoints
├── .env                    # Environment variables (not in version control)
├── templates/              # Jinja2 HTML templates
│   ├── base.html          # Base template with navbar and footer
│   ├── index.html         # Homepage with video grid
│   ├── watch.html         # Video player page
│   └── upload.html        # Video upload form
├── static/                 # Static assets
│   └── style.css          # Main stylesheet with dark theme
└── README.md              # This file
```

### Running the Application:

**Using Python:**
```bash
cd Day_29
python -m uvicorn main:app --reload
```

**Using UV:**
```bash
cd Day_29
uv run fastapi dev main.py
```

Application runs on: `http://127.0.0.1:8000`

### API Endpoints:

#### GET Endpoints:
- `GET /`: Homepage displaying all uploaded videos in a grid
- `GET /videos/{video_name}`: Stream video file with HTTP range support
- `GET /watch/{video_name}`: Video player page for watching a specific video
- `GET /upload`: Video upload form page

#### POST Endpoints:
- `POST /upload`: Handle video file upload to Supabase Storage
  - Form fields: `title` (string), `video_file` (file)
  - Automatically generates filename from title
  - Returns success/error message

### Key Implementation Details:

#### Video Streaming:
```python
async def video_stream():
    async with httpx.AsyncClient() as client:
        async with client.stream('GET', video_url, headers={'Range': 'bytes=0-'}, timeout=None) as response:
            async for chunk in response.aiter_bytes():
                yield chunk
```
- Uses async streaming for efficient memory usage
- Supports HTTP range requests for seeking
- Timeout set to None for large video files

#### File Upload:
```python
@app.post('/upload')
async def upload_video(request: Request, title: str = Form(...), video_file: UploadFile = File(...)):
    contents = await video_file.read()
    file_extension = video_file.filename.split('.')[-1]
    file_name = f"{title.replace(' ', '_')}.{file_extension}"
    res = supabase.storage.from_(SUPABASE_BUCKET).upload(file_name, contents)
```
- Extracts file extension from uploaded file
- Creates clean filename from title (spaces → underscores)
- Uploads binary content to Supabase Storage

#### Supabase Integration:
```python
from supabase import create_client, Client

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# List videos
videos = supabase.storage.from_(SUPABASE_BUCKET).list()

# Get public URL
video_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(video_name)

# Upload file
res = supabase.storage.from_(SUPABASE_BUCKET).upload(file_name, contents)
```

### UI Features:

#### Modern Dark Theme:
- Netflix-inspired color palette
- Glassmorphism effects on navigation
- Smooth animations and transitions
- Responsive design (mobile to desktop)

#### Video Grid:
- Dynamic gradient thumbnails for each video
- Hover effects with play button overlay
- Automatic title extraction from filename
- Empty state when no videos exist

#### Video Player:
- Full-width responsive player
- Native HTML5 controls
- Keyboard shortcuts:
  - `Space`: Play/Pause
  - `Arrow Left`: Seek backward 5s
  - `Arrow Right`: Seek forward 5s
  - `F`: Toggle fullscreen

#### Upload Interface:
- Drag-and-drop file upload
- File preview with size display
- Visual upload progress indicator
- Success/error message notifications
- Form validation

### Files:

**Backend:**
- **main.py**: Complete FastAPI application with video streaming, upload, and template rendering

**Templates:**
- **base.html**: Base template with navigation, footer, and common layout
- **index.html**: Homepage with responsive video grid and empty state
- **watch.html**: Video player page with keyboard shortcuts
- **upload.html**: Upload form with drag-and-drop and progress indication

**Styling:**
- **style.css**: Comprehensive stylesheet with dark theme, animations, and responsive design

### Key Concepts:

#### Supabase Storage:
- **Object Storage**: S3-compatible storage for files and media
- **Public URLs**: Direct CDN URLs for public file access
- **Storage API**: Simple REST API for file operations
- **Bucket Management**: Organize files into separate buckets

#### Video Streaming:
- **HTTP Range Requests**: Enable seeking in video player
- **Chunked Transfer**: Stream large files efficiently
- **Async Streaming**: Non-blocking video delivery
- **StreamingResponse**: FastAPI's response type for streaming data

#### Template Rendering:
- **Jinja2**: Powerful template engine for Python
- **Template Inheritance**: Base templates with blocks for content
- **Context Variables**: Pass data from backend to templates
- **Filters**: Transform data in templates (e.g., string replacement)

#### Form Handling:
- **Multipart Forms**: Handle file uploads with form data
- **Form Fields**: `Form(...)` for text inputs, `File(...)` for file uploads
- **File Processing**: Read and process uploaded files
- **Validation**: Check file types and handle errors

### Security Considerations:

1. **Environment Variables**: Never commit `.env` file to version control
2. **File Validation**: Validate file types and sizes before upload
3. **Storage Permissions**: Configure proper bucket access policies
4. **API Keys**: Keep Supabase keys secure and use anon key for client-side
5. **Error Handling**: Don't expose sensitive information in error messages

### Performance Optimizations:

1. **Async Streaming**: Non-blocking video delivery for better concurrency
2. **CDN Delivery**: Supabase provides CDN for fast global access
3. **Chunked Uploads**: Handle large files efficiently
4. **Static File Serving**: FastAPI's StaticFiles for CSS/JS delivery
5. **Response Caching**: Browser caching for static assets

### Troubleshooting:

**Videos not loading:**
- Check if bucket is set to public in Supabase
- Verify SUPABASE_BUCKET name matches your bucket
- Ensure video files are uploaded correctly

**Upload fails:**
- Check file size limits in Supabase
- Verify SUPABASE_ANON_KEY has upload permissions
- Ensure multipart form encoding is correct

**Streaming issues:**
- Check CORS settings in Supabase
- Verify video format is supported (MP4, WebM)
- Ensure proper Content-Type headers

### Future Enhancements:

- **User Authentication**: Add login/signup with Supabase Auth
- **Video Thumbnails**: Generate and store video thumbnails
- **Categories/Tags**: Organize videos with metadata
- **Search Functionality**: Search videos by title or tags
- **Playlists**: Create and manage video playlists
- **Comments**: Add comment system for videos
- **Video Processing**: Transcode videos for different resolutions
- **Analytics**: Track video views and engagement

### Notes:

- Supabase Storage is free up to 1GB, with paid plans for more storage
- Video files should be in web-compatible formats (MP4 with H.264 codec recommended)
- The application uses server-side rendering for SEO and initial page load performance
- All frontend interactions are enhanced with vanilla JavaScript
- The dark theme reduces eye strain for extended viewing sessions
- Responsive design ensures great experience on all devices

### Real-World Applications:

This project demonstrates patterns used in production video platforms:
- **Educational Platforms**: Course video delivery systems
- **Content Management**: Internal video libraries for companies
- **Social Media**: User-generated video content platforms
- **Portfolio Sites**: Showcase video work and projects
- **Documentation**: Video tutorials and guides

### Best Practices Demonstrated:

1. **Separation of Concerns**: Templates, static files, and business logic separated
2. **Environment Configuration**: Secure credential management with dotenv
3. **Error Handling**: Graceful error handling with proper HTTP status codes
4. **Code Organization**: Clean, readable code with proper imports and structure
5. **User Experience**: Loading states, error messages, and visual feedback
6. **Responsive Design**: Mobile-first approach with breakpoints
7. **Accessibility**: Semantic HTML and proper ARIA labels
8. **Performance**: Async operations and efficient file handling

---
# Day-30

## Intermediate Social Media Backend using FastAPI (Micro-Blogging Site) (Folder: Day_30)

This application demonstrates building an intermediate-level social media backend using FastAPI, implementing core features like user management, posts, likes, retweets, follows, and JWT authentication. It showcases advanced FastAPI patterns including modular routing, dependency injection, custom exceptions, and comprehensive database relationships.

### Learning Goals:
1. Build a complete social media backend with modern architecture
2. Implement JWT authentication with proper security practices
3. Work with complex database relationships (many-to-many, foreign keys)
4. Create modular FastAPI applications with proper separation of concerns
5. Handle custom exceptions and error responses
6. Use Pydantic for data validation and serialization
7. Implement CRUD operations with proper authorization

### What is a Micro-Blogging Site?

- **Social Media Platform**: Twitter/X-like platform for short-form content
- **Real-time Interactions**: Like, retweet, and follow functionality
- **User Authentication**: Secure user registration and login
- **Content Management**: Create, read, update, delete posts
- **Social Features**: Follow/unfollow users, view timelines

### Key Features Demonstrated:

#### User Management:
- **User Registration**: Secure signup with password hashing
- **JWT Authentication**: Token-based authentication with expiration
- **User Profiles**: Basic user information management
- **Follow System**: Many-to-many relationships for following users

#### Content Management:
- **Post Creation**: Create text-based posts with character limits
- **Post Updates**: Edit posts within a time window (10 minutes)
- **Post Deletion**: Delete own posts with authorization checks
- **Timeline**: View posts from followed users

#### Social Interactions:
- **Like System**: Like/unlike posts with duplicate prevention
- **Retweet System**: Retweet/unretweet posts
- **Follow/Unfollow**: Follow and unfollow other users
- **Engagement Metrics**: Count likes and retweets per post

#### Advanced Features:
- **Custom Exceptions**: Centralized error handling with HTTP status codes
- **Modular Routing**: Separate routers for auth, users, and posts
- **Database Relationships**: Complex SQLAlchemy relationships
- **Pydantic Schemas**: Comprehensive data validation and serialization
- **Dependency Injection**: Clean dependency management with FastAPI

### Installation:

**Install dependencies:**
```bash
pip install fastapi uvicorn sqlalchemy python-jose[cryptography] passlib[bcrypt] python-multipart python-dotenv
```

Or using UV:
```bash
uv add fastapi uvicorn sqlalchemy python-jose passlib python-multipart python-dotenv
```

### Environment Setup:

Create a `.env` file in the Day_30 directory:
```env
DAY_30_SECURITY_KEY=your-secret-key-here
DAY_30_ALGORITHM=HS256
DAY_30_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Project Structure:
```
Day_30/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   ├── database.py             # SQLAlchemy database configuration
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic data models
│   ├── auth.py                 # JWT authentication utilities
│   ├── exceptions.py           # Custom exception handlers
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication endpoints
│   │   ├── users.py            # User management endpoints
│   │   └── posts.py            # Post management endpoints
│   └── microblog.db            # SQLite database file
├── .env                        # Environment variables
└── README.md                   # This file
```

### Database Models:

#### User Model:
```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(250), unique=True, index=True, nullable=False)
    hashed_password = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    posts = relationship("Post", back_populates="owner")
    followers = relationship("User", secondary=follow, ...)
```

#### Post Model:
```python
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(500), nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="posts")
    likes = relationship("Like", back_populates="post")
    retweets = relationship("Retweet", back_populates="post")
```

#### Like and Retweet Models:
```python
class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)

class Retweet(Base):
    __tablename__ = "retweets"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id"), primary_key=True)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
```

### Running the Application:

**Using Python:**
```bash
cd Day_30
python -m uvicorn app.main:app --reload
```

**Using UV:**
```bash
cd Day_30
uv run fastapi dev app/main.py
```

Application runs on: `http://127.0.0.1:8000`

### API Endpoints:

#### Authentication Routes (`/token`):
- `POST /token`: Login and get access token (OAuth2 form data)

#### User Routes (`/users`):
- `POST /users/`: Create a new user account
- `POST /users/{user_id}/follow`: Follow a user
- `POST /users/{user_id}/unfollow`: Unfollow a user

#### Post Routes (`/posts`):
- `GET /posts/`: Get posts with pagination (skip, limit)
- `GET /posts/with_counts/`: Get posts with like/retweet counts and owner usernames
- `POST /posts/`: Create a new post (requires authentication)
- `PUT /posts/{post_id}`: Update a post (requires ownership, within 10 minutes)
- `DELETE /posts/{post_id}`: Delete a post (requires ownership)
- `POST /posts/{post_id}/like`: Like a post
- `POST /posts/{post_id}/unlike`: Unlike a post
- `POST /posts/{post_id}/retweet`: Retweet a post
- `POST /posts/{post_id}/unretweet`: Unretweet a post

### Key Implementation Details:

#### JWT Authentication:
```python
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECURITY_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # Decode token and validate user
    user = db.query(models.User).filter(models.User.username == username).first()
    return user
```

#### Custom Exceptions:
```python
def raise_not_found_exception(detail: str = "Not Found"):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

def raise_forbidden_exception(detail: str = "Forbidden"):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=detail)

def raise_unauthorized_exception(detail: str = "Unauthorized"):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail=detail, 
        headers={"WWW-Authenticate": "Bearer"}
    )
```

#### Complex Queries:
```python
# Get posts with counts and owner usernames
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
```

#### Authorization Checks:
```python
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
    
    # Check 10-minute edit window
    post_timestamp_aware = post.timestamp.replace(tzinfo=timezone.utc)
    time_since_creation = datetime.now(timezone.utc) - post_timestamp_aware
    if time_since_creation > timedelta(minutes=10):
        raise exceptions.ForbiddenException("You are not allowed to update this post.")
```

### Pydantic Schemas:

#### User Schemas:
```python
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True
```

#### Post Schemas:
```python
class PostBase(BaseModel):
    content: str

class Post(PostBase):
    id: int
    timestamp: datetime
    owner_id: int

class PostWithCounts(Post):
    likes_count: int
    retweets_count: int
    owner_username: str
```

### Files:

**Core Application:**
- **main.py**: FastAPI application setup with router registration
- **database.py**: SQLAlchemy engine and session configuration
- **models.py**: Database models with relationships
- **schemas.py**: Pydantic models for request/response validation
- **auth.py**: JWT token creation and user authentication
- **exceptions.py**: Custom HTTP exception handlers

**Routes:**
- **auth.py**: Token generation endpoint
- **users.py**: User creation and follow/unfollow functionality
- **posts.py**: Complete CRUD operations for posts with social features

### Key Concepts:

#### Database Relationships:
- **One-to-Many**: User to Posts relationship
- **Many-to-Many**: User follows relationship using association table
- **One-to-Many**: Post to Likes/Retweets relationships

#### Authentication Flow:
- User registers with username, email, password
- Password is hashed using bcrypt
- User logs in with username/password
- JWT token is generated and returned
- Subsequent requests include token in Authorization header
- Token is validated on protected endpoints

#### Authorization Patterns:
- **Ownership Checks**: Users can only modify their own posts
- **Time-based Restrictions**: Posts can only be edited within 10 minutes
- **Duplicate Prevention**: Users cannot like/retweet the same post twice
- **Self-interaction Prevention**: Users cannot follow themselves

#### Error Handling:
- **Custom Exceptions**: Centralized error responses with appropriate HTTP codes
- **Validation Errors**: Pydantic handles input validation automatically
- **Database Errors**: Proper handling of database constraints and relationships

### Security Features:

1. **Password Hashing**: bcrypt for secure password storage
2. **JWT Tokens**: Stateless authentication with configurable expiration
3. **Input Validation**: Pydantic models prevent malicious input
4. **SQL Injection Prevention**: SQLAlchemy parameterized queries
5. **Authorization Checks**: Proper permission validation on all endpoints

### Performance Optimizations:

1. **Database Indexing**: Proper indexes on frequently queried columns
2. **Pagination**: Skip/limit parameters for large result sets
3. **Efficient Queries**: Subqueries for counting likes/retweets
4. **Connection Pooling**: SQLAlchemy session management

### Testing Considerations:

The application structure supports comprehensive testing:
- **Unit Tests**: Test individual functions and utilities
- **Integration Tests**: Test API endpoints with database
- **Authentication Tests**: Test JWT token validation
- **Authorization Tests**: Test permission checks
- **Database Tests**: Test relationships and constraints

### Production Considerations:

1. **Database Migration**: Use Alembic for schema migrations
2. **Environment Variables**: Secure credential management
3. **Rate Limiting**: Implement request rate limiting
4. **Logging**: Add comprehensive application logging
5. **Caching**: Implement Redis for session and data caching
6. **API Documentation**: Auto-generated docs with OpenAPI/Swagger
7. **Monitoring**: Add application performance monitoring

### Future Enhancements:

- **Real-time Updates**: WebSocket integration for live notifications
- **File Uploads**: Profile pictures and post media attachments
- **Search Functionality**: Full-text search for posts and users
- **Notifications**: Push notifications for interactions
- **Analytics**: User engagement and content performance metrics
- **Admin Panel**: Content moderation and user management
- **API Versioning**: Support multiple API versions
- **Caching Layer**: Redis for improved performance

### Real-World Applications:

This backend architecture is suitable for:
- **Social Media Platforms**: Twitter/X clones, micro-blogging sites
- **Content Platforms**: News aggregators, community forums
- **Professional Networks**: LinkedIn-style platforms
- **Educational Platforms**: Student-teacher interaction systems
- **Internal Tools**: Company communication platforms

### Best Practices Demonstrated:

1. **Clean Architecture**: Separation of concerns with modular design
2. **Type Safety**: Full type hints and Pydantic validation
3. **Error Handling**: Comprehensive exception management
4. **Security**: Proper authentication and authorization
5. **Database Design**: Normalized schema with proper relationships
6. **API Design**: RESTful endpoints with consistent patterns
7. **Code Organization**: Logical file structure and imports
8. **Documentation**: Comprehensive inline and external documentation

### Notes:

- The application uses SQLite for simplicity, but can be easily adapted to PostgreSQL/MySQL
- JWT tokens expire after 30 minutes by default (configurable)
- Posts can only be edited within a 10-minute window after creation
- Users cannot like/retweet their own posts (implicitly prevented)
- The follow system uses a many-to-many relationship with an association table
- All endpoints requiring authentication use dependency injection for current user
- Custom exceptions provide consistent error responses across the API
- The application demonstrates intermediate-level FastAPI patterns suitable for production use

This project serves as an excellent foundation for building more complex social media platforms, demonstrating how to structure a FastAPI application with proper authentication, authorization, and database relationships.

---
# Day-31

## FastAPI with Async SQLAlchemy and Neon Database (Folder: Day_31)

This application demonstrates building a high-performance FastAPI application using async SQLAlchemy with Neon database (a serverless PostgreSQL platform). It showcases modern async database operations, connection pooling, and load testing with Locust. The application provides a simple product management API with CRUD operations, demonstrating best practices for async database interactions in FastAPI.

### Learning Goals:
1. Implement async database operations with SQLAlchemy
2. Work with Neon database (serverless PostgreSQL)
3. Configure connection pooling for high-performance applications
4. Set up load testing with Locust
5. Use FastAPI lifespan events for database initialization
6. Handle async database sessions properly

### What is Neon Database?

- **Serverless PostgreSQL**: Fully managed PostgreSQL with automatic scaling
- **Branching**: Create database branches for development and testing
- **Auto-scaling**: Scales compute resources based on demand
- **Point-in-time Recovery**: Restore database to any point in time
- **Built-in Connection Pooling**: Optimized connection management
- **Real-time Performance**: Low-latency database operations

### Key Features Demonstrated:

#### Async Database Operations:
- **Async SQLAlchemy**: Non-blocking database operations with async/await
- **Connection Pooling**: Efficient connection management with pool_size and max_overflow
- **Async Sessions**: Proper async session handling with context managers
- **Lifespan Events**: Database initialization during FastAPI startup

#### Performance Optimization:
- **Connection Pooling**: Configured pool_size=20, max_overflow=0 for optimal performance
- **Pool Recycling**: Automatic connection recycling every hour
- **Async Operations**: Non-blocking I/O for better concurrency
- **Efficient Queries**: Optimized SQL queries with proper indexing

#### Load Testing:
- **Locust Integration**: Distributed load testing framework
- **Realistic Scenarios**: Simulates user behavior with weighted tasks
- **Performance Monitoring**: Track response times and error rates
- **Scalability Testing**: Test application performance under load

### Installation:

**Install dependencies:**
```bash
pip install fastapi uvicorn sqlalchemy[asyncio] asyncpg python-dotenv locust
```

Or using UV:
```bash
uv add fastapi uvicorn sqlalchemy asyncpg python-dotenv locust
```

### Environment Setup:

Create a `.env` file in the Day_31 directory:
```env
DAY_31_NEON_DATABASE_URL=postgresql+asyncpg://username:password@hostname/database
```

### Neon Database Setup:

1. **Create Neon Account**: Sign up at [neon.tech](https://neon.tech)
2. **Create Project**: Set up a new PostgreSQL project
3. **Get Connection String**: Copy the connection string from the dashboard
4. **Configure Environment**: Add the connection string to your `.env` file

### Project Structure:
```
Day_31/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application with async endpoints
│   ├── database.py             # Async SQLAlchemy configuration
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   └── locustfile.py           # Load testing configuration
├── .env                        # Environment variables
└── README.md                   # This file
```

### Database Model:

#### Product Model:
```python
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
```

### Pydantic Schemas:

#### Product Schemas:
```python
class ProductCreate(BaseModel):
    name: str
    price: float

class ProductRead(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True
```

### Running the Application:

**Using Python:**
```bash
cd Day_31
python -m uvicorn app.main:app --reload
```

**Using UV:**
```bash
cd Day_31
uv run fastapi dev app/main.py
```

Application runs on: `http://127.0.0.1:8000`

### API Endpoints:

#### GET Endpoints:
- `GET /`: Welcome message
- `GET /products`: List all products
- `GET /products/{product_id}`: Get a specific product by ID

#### POST Endpoints:
- `POST /products`: Create a new product

### Key Implementation Details:

#### Async Database Configuration:
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
    pool_size=20,        # Maximum number of connections in pool
    max_overflow=0,      # No overflow connections
    pool_recycle=3600,   # Recycle connections every hour
)

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
```

#### FastAPI Lifespan Events:
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await get_db()  # Initialize database tables
    yield

app = FastAPI(lifespan=lifespan)
```

#### Async CRUD Operations:
```python
@app.post("/products", response_model=ProductRead)
async def create_product(
    product: ProductCreate,
    session: AsyncSession = Depends(get_session),
):
    stmt = insert(Product).values(
        name=product.name, 
        price=product.price
    ).returning(Product)
    
    result = await session.execute(stmt)
    new_product = result.scalar_one_or_none()
    
    if not new_product:
        raise HTTPException(status_code=400, detail="Product not created")
    
    await session.commit()
    return new_product
```

### Load Testing with Locust:

#### Locust Configuration:
```python
from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(0.1, 1)  # Random wait between 0.1-1 seconds
    
    def on_start(self):
        self.client.get("/")  # Initial request when user starts

    @task(1)
    def get_products(self):
        # Task weight: 1 (lower priority)
        if self.product_ids:
            product_id = random.choice(list(self.product_ids))
        else:
            product_id = random.randint(1, 10)
        self.client.get(f"/products/{product_id}")

    @task(2)
    def create_product(self):
        # Task weight: 2 (higher priority)
        payload = {
            "name": f"Product {random.randint(1, 10000)}",
            "price": round(random.uniform(10.0, 100.0), 2)
        }
        response = self.client.post("/products", json=payload)
        if response.status_code == 200:
            product = response.json()
            self.product_ids.add(product["id"])

    @task(3)
    def list_products(self):
        # Task weight: 3 (highest priority)
        self.client.get("/products")
```

#### Running Load Tests:

**Start Locust Web Interface:**
```bash
cd Day_31
locust -f app/locustfile.py --host=http://127.0.0.1:8000
```

**Access Locust UI:**
- Open browser to `http://localhost:8089`
- Set number of users and spawn rate
- Start the load test
- Monitor real-time statistics

**Command Line Load Testing:**
```bash
locust -f app/locustfile.py --host=http://127.0.0.1:8000 --users=10 --spawn-rate=2 --run-time=30s
```

### Performance Metrics:

The load testing setup provides insights into:
- **Response Times**: Average, median, 95th percentile
- **Requests per Second**: Throughput measurement
- **Error Rates**: Failed request percentages
- **User Simulation**: Realistic user behavior patterns

### Database Optimization:

#### Connection Pool Configuration:
- **pool_size=20**: Maintain 20 persistent connections
- **max_overflow=0**: No additional connections beyond pool size
- **pool_recycle=3600**: Refresh connections hourly to prevent stale connections
- **echo=False**: Disable SQL query logging for performance

#### Async Session Management:
```python
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
```

### Files:

**Core Application:**
- **main.py**: FastAPI application with async endpoints and lifespan management
- **database.py**: Async SQLAlchemy engine configuration with connection pooling
- **models.py**: Product model with proper indexing
- **schemas.py**: Pydantic models for request/response validation

**Testing:**
- **locustfile.py**: Load testing configuration with realistic user scenarios

### Key Concepts:

#### Async SQLAlchemy:
- **create_async_engine**: Creates async database engine
- **AsyncSession**: Async database session for non-blocking operations
- **async_sessionmaker**: Factory for creating async sessions
- **execute()**: Async method for executing SQL statements

#### Connection Pooling:
- **Pool Size**: Number of persistent connections
- **Max Overflow**: Additional connections when pool is full
- **Pool Recycle**: Connection refresh interval
- **Pool Pre-ping**: Connection health checks

#### Lifespan Events:
- **@asynccontextmanager**: Decorator for async context managers
- **lifespan parameter**: FastAPI lifespan event handler
- **Database Initialization**: Create tables on startup

#### Load Testing:
- **HttpUser**: Base class for HTTP-based load testing
- **@task decorator**: Define user actions with weights
- **wait_time**: Simulate realistic user think time
- **on_start()**: Setup actions when user starts

### Performance Benefits:

1. **Async Operations**: Non-blocking I/O improves concurrency
2. **Connection Pooling**: Reduces connection overhead
3. **Optimized Queries**: Efficient database operations
4. **Load Testing**: Identify performance bottlenecks early

### Production Considerations:

1. **Database Scaling**: Neon automatically scales with demand
2. **Monitoring**: Track query performance and connection usage
3. **Backup Strategy**: Neon provides automatic backups
4. **Security**: Use environment variables for sensitive data
5. **Rate Limiting**: Implement request rate limiting if needed
6. **Caching**: Add Redis caching for frequently accessed data

### Future Enhancements:

- **Authentication**: Add JWT authentication for secure access
- **Pagination**: Implement cursor-based pagination for large datasets
- **Search**: Add full-text search capabilities
- **Caching**: Integrate Redis for improved performance
- **Monitoring**: Add application performance monitoring
- **API Versioning**: Support multiple API versions
- **Background Tasks**: Add async background job processing

### Real-World Applications:

This architecture is suitable for:
- **E-commerce Platforms**: Product catalog management
- **SaaS Applications**: Multi-tenant data management
- **Real-time Dashboards**: High-concurrency data access
- **API Gateways**: High-throughput service backends
- **Data Analytics**: Fast data retrieval and processing

### Best Practices Demonstrated:

1. **Async First**: Use async operations for better performance
2. **Connection Pooling**: Optimize database connection management
3. **Load Testing**: Test application performance under realistic conditions
4. **Environment Configuration**: Secure credential management
5. **Error Handling**: Proper HTTP exception handling
6. **Type Safety**: Pydantic models for data validation
7. **Code Organization**: Clean separation of concerns

### Notes:

- Neon database provides excellent performance for both development and production
- Async SQLAlchemy operations are crucial for high-performance FastAPI applications
- Connection pooling configuration should be tuned based on application needs
- Load testing helps identify performance bottlenecks before production deployment
- The application demonstrates modern async Python patterns suitable for scalable applications

This project showcases how to build high-performance FastAPI applications with async database operations, proper connection management, and comprehensive load testing, making it an excellent foundation for production-ready applications.

---
# Day-32

## AI Agents that Debate Each Other Using Pydantic AI (Folder: Day_32)

This application demonstrates building an AI-powered debate system using FastAPI and Pydantic AI. It features two opposing AI agents (representing Donald Trump and Joe Biden) that engage in structured debates on given topics. Each agent incorporates a research sub-agent to gather relevant information before formulating their responses, creating a multi-agent architecture for enhanced reasoning and argumentation.

### Learning Goals:
1. Build multi-agent AI systems with Pydantic AI
2. Implement structured debate workflows between AI agents
3. Use FastAPI to create AI-powered API endpoints
4. Understand agent composition and hierarchical agent architectures
5. Handle asynchronous AI operations in web applications

### What is Pydantic AI?

**Pydantic AI** is a Python framework for building production-ready AI applications with type safety and structured data handling. It provides:

- **Type-Safe AI**: Full type hints and Pydantic validation for AI interactions
- **Agent Composition**: Build complex multi-agent systems
- **Structured Outputs**: Ensure AI responses follow specific schemas
- **Error Handling**: Robust error handling for AI operations
- **Async Support**: Native async/await support for concurrent AI operations
- **Model Agnostic**: Works with OpenAI, Anthropic, and other LLM providers

### Key Features Demonstrated:

#### Multi-Agent Architecture:
- **Primary Agents**: Two main debate agents (Trump and Biden personas)
- **Research Sub-Agents**: Each primary agent has a research agent for information gathering
- **Hierarchical Structure**: Agents can spawn sub-agents for specialized tasks
- **Message Storage**: Persistent storage of debate exchanges

#### AI Debate System:
- **Political Personas**: Agents embody distinct political ideologies
- **Structured Responses**: Consistent response formats from each agent
- **Topic Analysis**: Agents research and analyze debate topics
- **Argument Construction**: Logical argumentation based on gathered information

#### FastAPI Integration:
- **Async Endpoints**: Non-blocking AI operations
- **Query Parameters**: Simple API for debate initiation
- **JSON Responses**: Structured output with agent responses
- **Error Handling**: Graceful handling of AI operation failures

### Installation:

**Install dependencies:**
```bash
pip install fastapi uvicorn pydantic-ai openai python-dotenv
```

Or using UV:
```bash
uv add fastapi uvicorn pydantic-ai openai python-dotenv
```

### Environment Setup:

Create a `.env` file in the Day_32 directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Project Structure:
```
Day_32/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   └── debate/
│       ├── __init__.py
│       ├── agents.py           # AI agent definitions and configurations
│       └── service.py          # Debate orchestration service
├── .env                        # Environment variables
└── README.md                   # This file
```

### AI Agent Architecture:

#### Primary Agents:

**Right-Wing Agent (Donald Trump Persona):**
```python
right_wing_agent = Agent(
    'openai:gpt-4o',
    deps_type=str,
    result_type=str,
    system_prompt="""
    You are Donald Trump. You must respond in the first person, using Trump's distinctive speaking style:
    - Use simple, direct language
    - Repeat key phrases for emphasis
    - Be confident and assertive
    - Use superlatives (tremendous, fantastic, huge)
    - Reference your achievements and deals
    - Be critical of opponents and the 'fake news media'
    - Use phrases like "tremendous," "the best," "nobody does it better"
    """
)
```

**Left-Wing Agent (Joe Biden Persona):**
```python
left_wing_agent = Agent(
    'openai:gpt-4o',
    deps_type=str,
    result_type=str,
    system_prompt="""
    You are Joe Biden. You must respond in the first person, using Biden's distinctive speaking style:
    - Use folksy, relatable language
    - Be optimistic and unifying
    - Reference working families and middle class
    - Use phrases like "here's the deal," "God love ya," "malarkey"
    - Show empathy and understanding
    - Focus on unity and American values
    - Reference your long career in public service
    """
)
```

#### Research Sub-Agents:

Each primary agent includes a research sub-agent:
```python
research_agent = Agent(
    'openai:gpt-4o',
    deps_type=str,
    result_type=str,
    system_prompt="""
    You are a research assistant. Your job is to:
    1. Research the given topic thoroughly
    2. Gather relevant facts, statistics, and context
    3. Provide balanced information for debate preparation
    4. Focus on accuracy and comprehensiveness
    """
)
```

### Running the Application:

**Using Python:**
```bash
cd Day_32
python -m uvicorn app.main:app --reload
```

**Using UV:**
```bash
cd Day_32
uv run fastapi dev app/main.py
```

Application runs on: `http://127.0.0.1:8000`

### API Endpoints:

#### GET Endpoints:
- `GET /debate?query={topic}`: Initiate a debate on a given topic

### Key Implementation Details:

#### Agent Execution Flow:
```python
async def analyze_profile(query: str) -> str:
    # Right-wing agent researches and responds
    result_right = await right_wing_agent.run("Here is the debate topic", deps=query)
    message_storage.append({"agent_type": "right_wing", "message": result_right.output})

    # Left-wing agent researches and responds
    result_left = await left_wing_agent.run("Here is the debate topic", deps=query)
    message_storage.append({"agent_type": "left_wing", "message": result_left.output})

    return {
        "Donald Trump Thoughts": result_right.output,
        "Joe Biden Thoughts": result_left.output
    }
```

#### Message Storage:
```python
message_storage = []  # Global storage for debate exchanges

# Each agent response is stored with metadata
message_storage.append({
    "agent_type": "right_wing",
    "message": result_right.output
})
```

#### FastAPI Integration:
```python
from fastapi import FastAPI
from app.debate.service import analyze_profile

app = FastAPI()

@app.get("/debate")
async def pass_in_debate_data(query: str):
    result = await analyze_profile(query)
    return result
```

### Example Usage:

**Request:**
```
GET /debate?query=climate%20change%20policy
```

**Response:**
```json
{
  "Donald Trump Thoughts": "Climate change? It's a hoax! The best scientists, tremendous scientists, they tell me it's not a problem. China and India are polluting like crazy, but we're supposed to pay? No way! I made the best deals, nobody does it better than me. We'll have clean air, clean water, but we won't get ripped off by the fake news media and the radical Democrats!",
  "Joe Biden Thoughts": "Folks, climate change is real, and it's an existential threat to our planet. Here's the deal - we need to work together as Americans to tackle this crisis. I've been fighting for the environment my whole career, from the Clean Air Act to the Paris Agreement. We can create millions of good-paying jobs in clean energy while protecting our kids' future. God love ya, but we can't afford to wait any longer!"
}
```

### AI Agent Capabilities:

#### Research Integration:
- **Information Gathering**: Agents research topics before debating
- **Fact-Based Arguments**: Responses grounded in researched information
- **Context Awareness**: Understanding of current events and historical context
- **Balanced Analysis**: Research provides comprehensive topic coverage

#### Personality Emulation:
- **Authentic Personas**: Agents embody real political figures' communication styles
- **Consistent Voice**: Maintains character throughout the debate
- **Rhetorical Devices**: Uses appropriate rhetorical techniques
- **Emotional Intelligence**: Appropriate emotional responses to topics

#### Debate Structure:
- **Opening Statements**: Initial positions on the topic
- **Evidence Presentation**: Supporting arguments with facts
- **Counterarguments**: Addressing opposing viewpoints
- **Closing Remarks**: Summarizing key points

### Files:

**Core Application:**
- **main.py**: FastAPI application with debate endpoint
- **debate/agents.py**: AI agent definitions and configurations
- **debate/service.py**: Debate orchestration and message handling

### Key Concepts:

#### Pydantic AI Agents:
- **Agent Class**: Core building block for AI interactions
- **System Prompts**: Define agent behavior and personality
- **Dependencies**: Type-safe data passing between agents
- **Result Types**: Structured output validation

#### Multi-Agent Systems:
- **Agent Composition**: Building complex systems from simpler agents
- **Hierarchical Agents**: Parent-child agent relationships
- **Message Passing**: Communication between agents
- **State Management**: Maintaining conversation context

#### Async AI Operations:
- **Non-blocking Calls**: Concurrent AI model interactions
- **Resource Management**: Efficient handling of API rate limits
- **Error Resilience**: Graceful handling of AI service failures
- **Performance Optimization**: Parallel agent execution

### Advanced Features:

#### Agent Customization:
- **Dynamic Prompts**: Context-aware system prompt generation
- **Personality Scaling**: Adjustable personality intensity
- **Topic Adaptation**: Topic-specific response strategies
- **Learning Integration**: Potential for conversation memory

#### Debate Enhancement:
- **Multi-round Debates**: Extended conversations between agents
- **Moderator Agent**: Neutral agent to facilitate discussions
- **Fact-checking Agent**: Verification of claims made during debate
- **Audience Analysis**: Sentiment analysis of debate reception

#### Scalability Considerations:
- **Agent Pooling**: Multiple instances of the same agent type
- **Load Balancing**: Distributing requests across agent instances
- **Caching**: Response caching for similar queries
- **Rate Limiting**: Managing API usage costs

### Production Considerations:

1. **API Cost Management**: Monitor OpenAI API usage and costs
2. **Response Caching**: Cache responses for frequently debated topics
3. **Content Moderation**: Implement safeguards for sensitive topics
4. **Rate Limiting**: Prevent abuse of the debate endpoint
5. **Logging and Monitoring**: Track agent performance and usage patterns
6. **Error Handling**: Robust error handling for AI service failures
7. **Security**: Input validation and sanitization
8. **Scalability**: Horizontal scaling for high-traffic scenarios

### Future Enhancements:

- **WebSocket Integration**: Real-time debate streaming
- **Multi-Agent Debates**: More than two agents in a debate
- **User Participation**: Human users joining AI debates
- **Debate History**: Persistent storage of debate transcripts
- **Voting System**: User voting on debate winners
- **Topic Suggestions**: AI-generated debate topic recommendations
- **Personality Customization**: User-defined agent personalities
- **Multi-language Support**: Debates in different languages

### Real-World Applications:

This AI debate system demonstrates patterns used in:
- **Educational Tools**: Teaching critical thinking and argumentation
- **Content Generation**: Automated content creation for media
- **Decision Support**: AI-assisted policy analysis and discussion
- **Entertainment**: AI-powered interactive storytelling
- **Research**: Automated literature review and analysis
- **Training**: AI tutors for debate and public speaking
- **Journalism**: Automated perspective generation for articles

### Best Practices Demonstrated:

1. **Type Safety**: Full type hints with Pydantic validation
2. **Async Programming**: Non-blocking AI operations
3. **Modular Design**: Separated concerns in agent/service architecture
4. **Error Handling**: Comprehensive error management
5. **Configuration Management**: Environment-based configuration
6. **Code Organization**: Logical file structure and imports
7. **Documentation**: Clear inline and external documentation

### Ethical Considerations:

1. **Bias Awareness**: Understanding potential biases in AI responses
2. **Fact Verification**: Importance of grounding AI responses in facts
3. **Transparency**: Clear indication that responses are AI-generated
4. **Responsible Use**: Appropriate applications for AI debate systems
5. **Content Guidelines**: Establishing boundaries for debate topics
6. **User Safety**: Protecting users from harmful or misleading content

### Performance Optimization:

1. **Concurrent Execution**: Running multiple agents simultaneously
2. **Response Caching**: Avoiding redundant API calls
3. **Prompt Optimization**: Efficient prompt engineering
4. **Model Selection**: Choosing appropriate AI models for the task
5. **Batch Processing**: Handling multiple debate requests efficiently

### Notes:

- The application uses OpenAI's GPT-4o model for high-quality responses
- Agents maintain consistent personas throughout debates
- Research sub-agents provide factual grounding for arguments
- The system demonstrates advanced multi-agent AI architectures
- Pydantic AI provides type safety and structured AI interactions
- The debate system can be extended to include more agents or topics
- Real-world applications require careful consideration of ethical implications
- The architecture is scalable and can handle complex multi-agent scenarios

This project showcases how to build sophisticated AI applications using FastAPI and Pydantic AI, demonstrating the power of multi-agent systems for complex reasoning and interaction tasks.

---
# Day-33

## Real-Time Notification System with FastAPI, WebSockets, and Async SQLAlchemy (Folder: Day_33)

This application demonstrates building a real-time notification system using FastAPI, WebSockets, async SQLAlchemy, and server-side templating with Jinja2. It showcases modern web development practices including real-time communication, async database operations, and responsive UI design. The system allows users to create notifications that are instantly broadcast to all connected WebSocket clients, providing a live notification feed.

### Learning Goals:
1. Implement real-time communication with WebSockets in FastAPI
2. Work with async SQLAlchemy for high-performance database operations
3. Build responsive web interfaces with server-side templating
4. Handle WebSocket connections and broadcasting
5. Create modern, interactive web applications with vanilla JavaScript
6. Implement proper error handling and connection management

### What is Real-Time Communication?

- **WebSockets**: Bidirectional communication protocol for real-time data exchange
- **Live Updates**: Instant notification delivery without page refreshes
- **Connection Management**: Handling multiple concurrent WebSocket connections
- **Broadcasting**: Sending messages to all connected clients simultaneously
- **Persistent Connections**: Maintaining long-lived connections for real-time features

### Key Features Demonstrated:

#### Backend Features:
- **Async Database Operations**: Non-blocking database interactions with async SQLAlchemy
- **WebSocket Integration**: Real-time bidirectional communication
- **Connection Manager**: Efficient handling of multiple WebSocket connections
- **Broadcast System**: Instant message delivery to all connected clients
- **RESTful API**: Traditional HTTP endpoints for notification management
- **Lifespan Events**: Proper application startup and database initialization

#### Frontend Features:
- **Real-Time Updates**: Live notification feed without page refreshes
- **Responsive Design**: Modern, mobile-friendly interface
- **Interactive Forms**: Dynamic form submission with loading states
- **Connection Status**: Visual WebSocket connection indicators
- **Auto-Reconnection**: Automatic reconnection on connection loss
- **Animation Effects**: Smooth UI transitions and visual feedback

#### Database Features:
- **Async SQLAlchemy**: High-performance async database operations
- **Neon Database**: Serverless PostgreSQL with automatic scaling
- **Connection Pooling**: Efficient database connection management
- **Migration Support**: Automatic table creation on startup

### Installation:

**Install dependencies:**
```bash
pip install fastapi uvicorn sqlalchemy[asyncio] asyncpg python-dotenv jinja2
```

Or using UV:
```bash
uv add fastapi uvicorn sqlalchemy asyncpg python-dotenv jinja2
```

### Environment Setup:

Create a `.env` file in the Day_33 directory:
```env
DAY_33_NEON_DATABASE_URL=postgresql+asyncpg://username:password@hostname/database
```

### Neon Database Setup:

1. **Create Neon Account**: Sign up at [neon.tech](https://neon.tech)
2. **Create Project**: Set up a new PostgreSQL project
3. **Get Connection String**: Copy the connection string from the dashboard
4. **Configure Environment**: Add the connection string to your `.env` file

### Project Structure:
```
Day_33/
├── app/
│   ├── main.py                 # FastAPI application with WebSocket endpoints
│   ├── database.py             # Async SQLAlchemy configuration
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic schemas
│   └── templates/
│       ├── base.html          # Base template with common layout
│       └── index.html         # Main page with notification interface
├── .env                        # Environment variables
└── README.md                   # This file
```

### Database Model:

#### Notification Model:
```python
class Notification(Base):
    __tablename__ = 'notifications'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
```

### Pydantic Schemas:

#### Notification Schemas:
```python
class NotificationCreate(BaseModel):
    user_id: int
    message: str

class NotificationRead(BaseModel):
    id: int
    user_id: int
    message: str
    created_at: datetime

    class Config:
        orm_mode = True
```

### Running the Application:

**Using Python:**
```bash
cd Day_33
python -m uvicorn app.main:app --reload
```

**Using UV:**
```bash
cd Day_33
uv run fastapi dev app/main.py
```

Application runs on: `http://127.0.0.1:8000`

### API Endpoints:

#### GET Endpoints:
- `GET /`: Homepage displaying the notification interface
- `GET /notifications`: Retrieve the last 7 notifications (JSON response)

#### POST Endpoints:
- `POST /notifications`: Create a new notification and broadcast it via WebSocket

#### WebSocket Endpoints:
- `WebSocket /ws`: Real-time WebSocket connection for live updates

### Key Implementation Details:

#### WebSocket Connection Management:
```python
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                disconnected.append(connection)
        for connection in disconnected:
            self.disconnect(connection)
```

#### FastAPI Lifespan Events:
```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # Initialize database tables
    yield

app = FastAPI(lifespan=lifespan)
```

#### Notification Creation with Broadcasting:
```python
@app.post("/notifications", response_model=NotificationRead)
async def create_notification(
    notif: NotificationCreate,
    session: AsyncSession = Depends(get_session)
):
    stmt = insert(Notification).values(
        user_id=notif.user_id,
        message=notif.message
    ).returning(Notification)

    result = await session.execute(stmt)
    new_notif = result.scalar_one()
    await session.commit()

    # Broadcast to all connected WebSocket clients
    message_to_broadcast = {
        "action": "new_notification",
        "data": {
            "id": new_notif.id,
            "user_id": new_notif.user_id,
            "message": new_notif.message
        }
    }
    await manager.broadcast(message_to_broadcast)

    return new_notif
```

#### WebSocket Endpoint:
```python
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

### Frontend Implementation:

#### Real-Time Updates:
```javascript
// WebSocket connection
function connectWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    ws = new WebSocket(`${protocol}//${window.location.host}/ws`);
    
    ws.onopen = () => {
        wsStatus.textContent = '✅ Connected - Real-time updates active';
        wsStatus.className = 'connected';
    };
    
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.action === 'new_notification') {
            addNotificationToList(data.data, true);
        }
    };
    
    ws.onclose = () => {
        wsStatus.textContent = '❌ Disconnected - Attempting to reconnect...';
        setTimeout(connectWebSocket, 3000);
    };
}
```

#### Dynamic Notification Display:
```javascript
function addNotificationToList(notif, isNew) {
    const div = document.createElement('div');
    div.className = 'notification-item' + (isNew ? ' new' : '');
    
    div.innerHTML = `
        <div class="notification-header">
            <span class="user-badge">User #${notif.user_id}</span>
            <span class="timestamp">${new Date().toLocaleString()}</span>
        </div>
        <div class="message">${escapeHtml(notif.message)}</div>
    `;
    
    if (isNew) {
        notificationsList.insertBefore(div, notificationsList.firstChild);
    } else {
        notificationsList.appendChild(div);
    }
}
```

### UI Features:

#### Modern Dark Theme:
- Netflix-inspired color palette
- Glassmorphism effects and subtle shadows
- Smooth animations and transitions
- Responsive design (mobile to desktop)

#### Real-Time Interface:
- Live connection status indicator
- Instant notification updates
- Form submission with loading states
- Auto-reconnection on disconnection
- Highlight animations for new notifications

#### Interactive Elements:
- Drag-and-drop file upload (if extended)
- Keyboard shortcuts for enhanced UX
- Loading states and error handling
- Mobile-responsive design

### Files:

**Backend:**
- **main.py**: FastAPI application with WebSocket support and notification endpoints
- **database.py**: Async SQLAlchemy configuration with Neon database
- **models.py**: Notification model with proper indexing
- **schemas.py**: Pydantic models for request/response validation

**Frontend:**
- **templates/base.html**: Base template with navigation and common styling
- **templates/index.html**: Main interface with real-time notification system

### Key Concepts:

#### WebSocket Communication:
- **Bidirectional**: Full-duplex communication between client and server
- **Persistent Connections**: Long-lived connections for real-time features
- **Event-Driven**: Message-based communication with JSON payloads
- **Connection Lifecycle**: Proper handling of connect/disconnect events

#### Async Database Operations:
- **Non-blocking I/O**: Concurrent database operations without blocking
- **Connection Pooling**: Efficient management of database connections
- **Async Sessions**: Proper async session handling with context managers
- **Performance**: Better scalability with async operations

#### Server-Side Templating:
- **Jinja2**: Powerful template engine for Python
- **Template Inheritance**: Base templates with blocks for content
- **Dynamic Content**: Server-rendered HTML with data injection
- **Static Assets**: CSS and JavaScript integration

#### Real-Time Architecture:
- **Broadcast Pattern**: One-to-many message distribution
- **Connection Management**: Tracking and managing active connections
- **Error Resilience**: Graceful handling of connection failures
- **Scalability**: Foundation for horizontal scaling

### Security Considerations:

1. **Input Validation**: Pydantic models prevent malicious input
2. **XSS Prevention**: HTML escaping in templates and JavaScript
3. **Connection Limits**: Prevent excessive WebSocket connections
4. **Rate Limiting**: Implement request rate limiting for API endpoints
5. **Authentication**: Add user authentication for production use
6. **Data Sanitization**: Clean user input before database storage

### Performance Optimizations:

1. **Async Operations**: Non-blocking I/O for better concurrency
2. **Connection Pooling**: Efficient database connection management
3. **Message Batching**: Group multiple notifications for broadcast
4. **Caching**: Implement caching for frequently accessed data
5. **Compression**: Enable WebSocket message compression
6. **Load Balancing**: Distribute connections across multiple servers

### Production Considerations:

1. **WebSocket Scaling**: Use Redis for cross-server broadcasting
2. **Database Optimization**: Add proper indexing and query optimization
3. **Monitoring**: Implement application performance monitoring
4. **Logging**: Add comprehensive logging for debugging
5. **Security**: Implement proper authentication and authorization
6. **Backup**: Set up database backup and recovery procedures
7. **Testing**: Add comprehensive unit and integration tests

### Future Enhancements:

- **User Authentication**: Add login/signup with JWT tokens
- **Notification History**: Persistent storage with pagination
- **Push Notifications**: Browser push notifications for offline users
- **Notification Types**: Different notification categories and priorities
- **User Management**: User profiles and notification preferences
- **Analytics**: Track notification engagement and user behavior
- **Mobile App**: Native mobile application with push notifications
- **Admin Panel**: Notification management and user administration

### Real-World Applications:

This real-time notification system demonstrates patterns used in:
- **Social Media Platforms**: Live feed updates and notifications
- **Chat Applications**: Real-time messaging and presence indicators
- **Collaborative Tools**: Live document editing and comments
- **Gaming Platforms**: Live score updates and multiplayer interactions
- **Financial Applications**: Real-time price updates and alerts
- **IoT Dashboards**: Live sensor data and device status updates
- **News Platforms**: Breaking news alerts and live updates

### Best Practices Demonstrated:

1. **Async First**: Use async operations for better performance
2. **Clean Architecture**: Separation of concerns with modular design
3. **Error Handling**: Comprehensive exception handling and user feedback
4. **Real-Time Communication**: Proper WebSocket implementation
5. **Responsive Design**: Mobile-first approach with modern UI
6. **Security**: Input validation and XSS prevention
7. **Scalability**: Foundation for high-concurrency applications

### Notes:

- The application uses Neon database for reliable, serverless PostgreSQL
- WebSocket connections provide instant, real-time updates
- Async SQLAlchemy ensures high performance with concurrent operations
- The UI is fully responsive and works across all devices
- Connection management handles disconnections gracefully
- Broadcasting ensures all connected clients receive updates simultaneously
- The architecture is scalable and can handle multiple concurrent users
- Perfect for applications requiring real-time features and live updates

This project showcases how to build modern, real-time web applications using FastAPI's WebSocket support, async database operations, and responsive web interfaces, providing a solid foundation for applications requiring live communication and instant updates.

---
# Day-34

## FastAPI Application which follows all the best practices (Folder: Day_34)
This contains the following layers
- The Domain Layer
- The Application Layer
- The Infrastructure Layer
And unit testing and end to end testing
We would also be using Neon Database
For this we have taken 2 things: Todo and User (with proper authentication)