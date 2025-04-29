from pydantic import BaseModel, Field
from fastapi import UploadFile
from typing import Optional

class DocumentUploadRequest(BaseModel):
    document_type: str
    file:UploadFile

class DocumentResponse(BaseModel):
    id:str
    document_type: str
    document_id: str

class Document(BaseModel):
    id: Optional[str] = Field(default=None, exclude=True)
    document_type: str
    document_id: str
