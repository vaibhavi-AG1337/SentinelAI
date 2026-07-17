from fastapi import FastAPI, UploadFile, File
from app.models.schemas import MessageRequest
from app.agents.orchestrator_agent import process
from app.services.report_generator import generate_report
import os
import shutil
from app.database.database import engine
from app.database.models import Base

from app.utils.ocr import extract_text
from app.database.crud import save_scan
app = FastAPI(
    title="Sentinel AI",
    description="AI-Powered Phishing Detection System",
    version="1.0"
)
Base.metadata.create_all(bind=engine)

# -------------------------
# Home Route
# -------------------------

@app.get("/")
def home():
    return {
        "project": "Sentinel AI",
        "version": "1.0",
        "status": "Backend Running 🚀"
    }


# -------------------------
# Text Analysis Endpoint
# -------------------------

@app.post("/analyze")
def analyze(message: MessageRequest):

    result = process(message.text)
    save_scan(result, message.text)
    return result


# -------------------------
# Image Analysis Endpoint
# -------------------------
@app.post("/generate-report")
def create_report(message: MessageRequest):

    result = process(message.text)
    save_scan(result, extracted_text)
    generate_report(
        result,
        "sentinel_report.pdf"
    )

    return {
        "status": "Report Generated",
        "file": "sentinel_report.pdf"
    }

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):

    # Create uploads folder if it doesn't exist
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    # Save uploaded image
    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text using OCR
    extracted_text = extract_text(file_path)

    # Run Sentinel AI pipeline
    result = process(extracted_text)

    # Include extracted text in response
    result["extracted_text"] = extracted_text

    return result