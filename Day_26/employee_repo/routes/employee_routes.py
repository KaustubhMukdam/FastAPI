from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from ..database import supabase, SUPABASE_BUCKET, SUPABASE_URL
from ..models import EmployeeCreate, EmployeeUpdate
from ..forms import as_form
from fastapi.templating import Jinja2Templates
import uuid
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="./employee_repo/templates")

# --- API Endpoints ---

# --- GET Request Methods ---
@router.get("/", response_class=HTMLResponse)
async def read_employees(request: Request):
    response = supabase.table("employees").select("*").eq("is_active", True).execute()
    employees = response.data
    return templates.TemplateResponse("index.html", {"request": request, "employees": employees})

@router.get("/add", response_class=HTMLResponse)
async def add_employee_form(request: Request):
    return templates.TemplateResponse("add_employee.html", {"request": request})

@router.get("/edit/{employee_id}", response_class=HTMLResponse)
async def edit_employee_form(request: Request, employee_id: int):
    response = supabase.table("employees").select("*").eq("id", employee_id).execute()
    employee = response.data[0] if response.data else None
    return templates.TemplateResponse("edit_employee.html", {"request": request, "employee": employee})

# --- POST Request Methods ---
@router.post("/add")
async def add_employee(
    request: Request,
    employee: EmployeeCreate = Depends(EmployeeCreate.as_form),
    image: UploadFile = File(None)
):
    image_url = None
    if image and image.filename:
        # Generate unique filename to avoid conflicts
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        file_extension = image.filename.split('.')[-1] if '.' in image.filename else 'jpg'
        image_filename = f"{employee.first_name}_{employee.last_name}_{timestamp}_{unique_id}.{file_extension}"
        
        # Read file content
        file_content = await image.read()
        
        try:
            # Upload to Supabase storage
            response = supabase.storage.from_(SUPABASE_BUCKET).upload(
                path=image_filename,
                file=file_content,
                file_options={"content-type": image.content_type}
            )
            
            # Construct the public URL
            image_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{image_filename}"
        except Exception as e:
            print(f"Error uploading image: {e}")
            # Continue without image if upload fails

    # Insert employee data
    supabase.table("employees").insert({
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email": employee.email,
        "salary": employee.salary,
        "image_url": image_url
    }).execute()

    return RedirectResponse("/", status_code=303)

@router.post("/edit/{employee_id}")
async def edit_employee(
    request: Request,
    employee_id: int,
    employee: EmployeeUpdate = Depends(EmployeeUpdate.as_form),
    image: UploadFile = File(None)
):
    # Get current employee data
    current_employee = supabase.table("employees").select("*").eq("id", employee_id).execute()
    image_url = current_employee.data[0].get("image_url") if current_employee.data else None
    
    # Handle image upload if new image provided
    if image and image.filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        file_extension = image.filename.split('.')[-1] if '.' in image.filename else 'jpg'
        image_filename = f"{employee.first_name}_{employee.last_name}_{timestamp}_{unique_id}.{file_extension}"
        
        file_content = await image.read()
        
        try:
            response = supabase.storage.from_(SUPABASE_BUCKET).upload(
                path=image_filename,
                file=file_content,
                file_options={"content-type": image.content_type}
            )
            image_url = f"{SUPABASE_URL}/storage/v1/object/public/{SUPABASE_BUCKET}/{image_filename}"
        except Exception as e:
            print(f"Error uploading image: {e}")

    # Update employee data
    supabase.table("employees").update({
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email": employee.email,
        "salary": employee.salary,
        "is_active": employee.is_active,
        "image_url": image_url
    }).eq("id", employee_id).execute()

    return RedirectResponse("/", status_code=303)

# --- DELETE Request Methods ---
@router.post("/delete/{employee_id}")
async def delete_employee(request: Request, employee_id: int):
    supabase.table("employees").update({"is_active": False}).eq("id", employee_id).execute()
    return RedirectResponse("/", status_code=303)