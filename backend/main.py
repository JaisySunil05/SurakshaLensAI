from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import analyze_message

app = FastAPI()

# ✅ ADD THIS CORS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "SurakshaLens API Running"}

@app.post("/analyze")
def analyze(data: InputText):
    return analyze_message(data.message)