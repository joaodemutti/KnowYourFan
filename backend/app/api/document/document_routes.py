from fastapi import APIRouter, HTTPException, Depends,UploadFile,File,Form
from app.api.document.commands.upload_document import UploadDocumentHandler
from app.api.document.queries.validate_document import ValidateDocumentHandler
from app.api.document.queries.download_document import DownloadDocumentHandler
from app.api.document.queries.get_documents import GetDocumentsHandler
from app.models.document_model import DocumentUploadRequest
from app.api.auth.dependency import get_current_user

router = APIRouter()

@router.get("/documents")
async def get_documents(user_id: str = Depends(get_current_user)):
    return await GetDocumentsHandler(user_id).handle()

@router.post("/documents")
async def upload_document(document_type:str=Form(...),file:UploadFile=File(...),user_id: str = Depends(get_current_user)):
    handler = UploadDocumentHandler(user_id,DocumentUploadRequest(document_type=document_type,file=file))
    document_id = await handler.handle()
    return {"document_id": document_id}

@router.get("/documents/{document_id}/image")
async def download_document(document_id:str,user_id:str = Depends(get_current_user)):
    handler = DownloadDocumentHandler(document_id,user_id)
    return await handler.handle()

@router.post("/documents/{document_id}")
async def validate_document(document_id:str,user_id:str = Depends(get_current_user)):
    handler = ValidateDocumentHandler(document_id,user_id)
    return await handler.handle()