from fastapi import APIRouter, HTTPException
from app.api.document.commands.upload_document import UploadDocumentHandler
from app.api.document.queries.validate_document import ValidateDocumentHandler
from app.models.document_model import DocumentDTO

router = APIRouter()

@router.post("/documents")
async def upload_document(document: DocumentDTO):
    handler = UploadDocumentHandler(document_data=document)
    document_id = handler.handle()
    return {"document_id": document_id}

@router.get("/documents/{document_id}")
async def validate_document(document_id: str):
    handler = ValidateDocumentHandler(document_id=document_id)
    document = handler.handle()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document
