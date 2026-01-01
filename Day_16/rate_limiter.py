from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import time
from collections import defaultdict
from typing import Dict

app = FastAPI()

class AdvancedMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.rate_limit_records: Dict[str, float] = defaultdict(float)

    async def log_messages(self, message: str):
        print(message)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        last_request_time = self.rate_limit_records[client_ip]

        if current_time - last_request_time < 1:  # 1 second rate limit
            await self.log_messages(f"Rate limit exceeded for IP: {client_ip}")
            return Response(content="Too Many Requests", status_code=429)

        self.rate_limit_records[client_ip] = current_time
        path = request.url.path
        await self.log_messages(f"Request to {path} from IP: {client_ip} at {current_time}")
        
        #Process the request
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        # Add custom headers without overwriting existing ones
        custom_headers = {"X-Process-Time": str(process_time)} 
        for key, value in custom_headers.items():
            response.headers.append(key, value)

        #Async logging for processing time
        await self.log_messages(f"Processed request to {path} in {process_time} seconds")

        return response
    
# Add the advanced middleware to the FastAPI app
app.add_middleware(AdvancedMiddleware)

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get("/")
async def main_endpoint():
    return 'Welcome to FastAPI with Advanced Middleware example.'