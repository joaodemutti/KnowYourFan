import os
import uuid
from datetime import timedelta
from typing import Optional
from app.config.firebase_config import bucket 
from fastapi import UploadFile


async def upload_file(file:UploadFile, user_id: str, folder: str = "documents", make_public: bool = False) -> str:
    
    file_ext = os.path.splitext(file.filename)[1]
    file_id = f"{uuid.uuid4()}{file_ext}"
    file_name = f"{folder}/{user_id}/{file_id}"
    
    blob = bucket.blob(file_name)
    
    while blob.exists():
        file_id = f"{uuid.uuid4()}{file_ext}"
        file_name = f"{folder}/{user_id}/{file_id}"
        blob = bucket.blob(file_name)
    
    file_bytes = await file.read()
    blob.upload_from_string(file_bytes, content_type=file.content_type)

    return file_id


async def download_file(file_id, user_id: str, folder: str = "documents") -> bytes:

    file_name = f"{folder}/{user_id}/{file_id}"

    blob = bucket.blob(file_name)
    
    if not blob.exists():
        raise FileNotFoundError(f"The file with ID {file_id} does not exist in Firebase Storage.")

    return blob.download_as_string()