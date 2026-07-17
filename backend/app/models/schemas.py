from pydantic import BaseModel
from fastapi import UploadFile, File
class MessageRequest(BaseModel):
    text: str