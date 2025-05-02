from app.repositories.document_repository import DocumentRepository
from app.models.document_model import DocumentResponse
from app.services.storage_service import download_file
from fastapi.responses import FileResponse
from io import BytesIO
import os

class GetDocumentsQuery:
    def __init__(self,user_id:str):
        self.user_id = user_id

    async def execute(self):
        document_repository = DocumentRepository()
        documents = document_repository.get_documents(self.user_id)
        docs =[]
        for doc in documents:
            docs.append(DocumentResponse(**doc.model_dump(),id=doc.id))
        return docs
        
class GetDocumentsHandler:
    def __init__(self,user_id):
        self.user_id = user_id

    async def handle(self):
        command = GetDocumentsQuery(self.user_id)
        return await command.execute()
