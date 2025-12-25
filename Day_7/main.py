from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory=r"D:\Programming\FastAPI\Day_7\templates")

F1 = [{"name": "Max Verstappen", "team": "Red Bull"}, {"name": "Lewis Hamilton", "team": "Ferrari"}, {"name": "Charles Leclerc", "team": "Ferrari"}, {"name": "Kimi Antonelli", "team": "Mercedes"}, {"name": "Sergio Perez", "team": "Red Bull"}]

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get("/")
async def name (request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "message": "This is home page", "F1": F1})
