from fastapi import APIRouter, HTTPException, Depends
from app.api.document.commands.upload_document import UploadDocumentHandler
from app.api.document.queries.validate_document import ValidateDocumentHandler
from app.models.document_model import DocumentDTO
from app.api.auth.dependency import get_current_user

router = APIRouter()

@router.post("/documents")
async def upload_document(document: DocumentDTO,user_id: str = Depends(get_current_user)):
    handler = UploadDocumentHandler(document_data=document)
    document_id = handler.handle()
    return {"document_id": document_id}

@router.get("/documents/{document_id}")
async def validate_document(document_id: str,user_id: str = Depends(get_current_user)):
    handler = ValidateDocumentHandler(user_id=user_id,document_id=document_id)
    document = handler.handle()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
