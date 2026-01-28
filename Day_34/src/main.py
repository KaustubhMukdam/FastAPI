from fastapi import FastAPI
from .database.core import engine, Base
from .entities.todo import Todo
from .entities.user import User
from .api import register_routes
from .logging import configure_logging, LogLevels

configure_logging(LogLevels.info)

app = FastAPI()

# Create database tables
# While testing, we would comment this out to avoid recreating tables
# Base.metadata.create_all(bind=engine)

register_routes(app)