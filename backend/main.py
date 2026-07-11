from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "version": "0.1",
        "status": "Backend Running 🚀"
    }