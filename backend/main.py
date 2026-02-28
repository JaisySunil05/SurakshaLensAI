from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import analyze_message

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SurakshaLens API is running 🚀"}

class Message(BaseModel):
    message: str

@app.post("/analyze")
def analyze(msg: Message):
    return analyze_message(msg.message)