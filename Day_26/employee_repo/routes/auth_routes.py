from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from ..database import supabase
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="./employee_repo/templates")

# --- GET Request Methods ---
@router.get("/signup", response_class=HTMLResponse)
async def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/logout")
async def logout():
    response = RedirectResponse("/login", status_code=303)
    response.delete_cookie(key="access_token")
    return response

# --- POST Request Methods ---
@router.post("/signup")
async def signup(email: str = Form(...), password: str = Form(...)):
    try:
        auth_response = supabase.auth.sign_up({"email": email, "password": password})
        if auth_response.user is None:
            raise HTTPException(status_code=400, detail="User already exists")
        return RedirectResponse("/login", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    try:
        auth_response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if auth_response.user is None:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        access_token = auth_response.session.access_token
        response = RedirectResponse("/", status_code=303)
        response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True, samesite="lax")
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))