from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# --- API Endpoints ---

# --- GET Request Methods ---
@app.get("/")
async def hello():
    return {"message": "Hello World, FastAPI here"}

# Deployment commands in terminal
"""
pip3 install -t Day_8\dependencies -r requirements.txt
cd Day_8
cd dependencies
Compress-Archive -Path * -DestinationPath ..\lambda.zip -Force
cd ..
Compress-Archive -Path main.py -DestinationPath .\lambda.zip -Force (It adds the main.py file to the zip file)

"""
