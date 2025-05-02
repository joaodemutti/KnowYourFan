from pydantic import BaseModel, Field
from fastapi import UploadFile
from typing import Optional

class DocumentUploadRequest(BaseModel):
    type: str
    file:UploadFile

class DocumentResponse(BaseModel):
    id:str
    type: str
    valid:bool
    document_id: str

class Document(BaseModel):
    id: Optional[str] = Field(default=None, exclude=True)
    valid:bool = False
    type: str
    document_id: str
