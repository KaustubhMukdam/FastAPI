from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

class Logger:
    def log(self, message: str):
        print(f"Logging message: {message}")

def get_logger():
    return Logger()

logger_dependency = Annotated[Logger, Depends(get_logger)]

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get("/log/{message}")
def log_message(message: str, logger: Logger = Depends(get_logger)):
    logger.log(message)
    return {"message": message}

