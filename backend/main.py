from fastapi import FastAPI
from app.models.schemas import MessageRequest
from app.agents.orchestrator_agent import process
app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "version": "0.1",
        "status": "Backend Running 🚀"
    }
@app.post("/analyze")
def analyze(message: MessageRequest):

    return process(message.text)