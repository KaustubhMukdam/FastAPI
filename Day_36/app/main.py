from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.fitness_advisor.controller import router

app = FastAPI(title="Fitness Advisor API", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include router
app.include_router(router)