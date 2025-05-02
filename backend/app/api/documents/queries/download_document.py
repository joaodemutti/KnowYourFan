from app.repositories.document_repository import DocumentRepository
from app.services.storage_service import download_file
from fastapi.responses import StreamingResponse
from io import BytesIO
import os

class DownloadDocumentQuery:
    def __init__(self,document_id:str,user_id:str):
        self.document_id = document_id
        self.user_id = user_id

    async def execute(self):
        document_repository = DocumentRepository()

        document = document_repository.get_document(self.user_id,self.document_id)

        stream :bytes = await download_file(file_id=document.document_id,user_id=self.user_id)

        file = BytesIO(stream)
        ext=os.path.splitext(document.document_id)[1]
        file.name = f"image{ext}"
        return StreamingResponse(file,media_type=f"image/{ext[1:]}")
        
class DownloadDocumentHandler:
    def __init__(self,document_id,user_id):
        self.document_id = document_id
        self.user_id = user_id

    async def handle(self):
        command = DownloadDocumentQuery(self.document_id,self.user_id)
        return await command.execute()
