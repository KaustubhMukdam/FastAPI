from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.finance_advisor.controller import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Finance Advisor API", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include router
app.include_router(router)