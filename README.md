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

