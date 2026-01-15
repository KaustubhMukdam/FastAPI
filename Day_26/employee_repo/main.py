from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routes import employee_routes, auth_routes

app = FastAPI()

# Static file directory
app.mount("/static", StaticFiles(directory="./employee_repo/static"), name="static")

# Template directory
templates = Jinja2Templates(directory="./employee_repo/templates")

# Include routes
app.include_router(auth_routes.router)
app.include_router(employee_routes.router)