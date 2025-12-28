from fastapi import FastAPI 
from redis import Redis
import httpx
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

REDIS_URL = os.getenv("REDIS_URL")
@app.on_event("startup")
async def startup_event():
    app.state.redis = Redis(host='localhost', port=6379, db=0)
    app.state.http_client = httpx.AsyncClient()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.http_client.aclose()
    app.state.redis.close()

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get('/entries')
async def read_item():

    value = app.state.redis.get('entries')

    if value is None:
        response = await app.state.http_client.get('https://jsonplaceholder.typicode.com/posts')
        value = response.json()
        data_str = json.dumps(value)
        app.state.redis.set('entries', data_str)
    
    return json.loads(value)

