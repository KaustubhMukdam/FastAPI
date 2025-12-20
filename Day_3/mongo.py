#This file contains the FastAPI Application code
from fastapi import FastAPI
import urllib.parse
from routes.route import router

app = FastAPI()

app.include_router(router)