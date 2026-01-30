from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.finance_advisor.model import FinancialProfile
from app.finance_advisor.service import analyze_profile

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# --- API Endpoints ---

# --- GET Request Methods ---
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page with the financial profile form"""
    return templates.TemplateResponse("index.html", {"request": request})


# --- POST Request Methods ---
@router.post("/analyze")
async def analyze_finances(financial_profile: FinancialProfile):
    """Analyze the financial profile and return advice"""
    return await analyze_profile(financial_profile)