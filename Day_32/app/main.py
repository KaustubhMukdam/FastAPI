from fastapi import FastAPI
from app.debate.service import analyze_profile
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/debate")
async def pass_in_debate_data(query: str):
    result = await analyze_profile(query)
    return result