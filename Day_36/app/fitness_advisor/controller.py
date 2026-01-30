from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.fitness_advisor.service import analyze_profile
from app.fitness_advisor.model import FitnessProfile

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# --- Template Routes ---

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page"""
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/form", response_class=HTMLResponse)
async def fitness_form(request: Request):
    """Render the fitness profile form"""
    return templates.TemplateResponse("form.html", {"request": request})

@router.get("/result", response_class=HTMLResponse)
async def result_page(request: Request):
    """Render the result page"""
    return templates.TemplateResponse("result.html", {"request": request})

# --- API Endpoints ---

@router.post("/analyze")
async def analyze_fitness(fitness_profile: FitnessProfile):
    """API endpoint to analyze fitness profile and return results"""
    result = await analyze_profile(fitness_profile)
    return {"message": "Fitness analysis complete", "result": result}