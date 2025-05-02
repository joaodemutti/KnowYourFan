from app.repositories.document_repository import DocumentRepository
from app.services.storage_service import download_file
from app.services.google_service import validate_document_image_bytes
from io import BytesIO
import os

class ValidateDocumentCommand:
    def __init__(self, document_id: str, user_id: str):
        self.document_id = document_id
        self.user_id = user_id

    async def execute(self):
        document_repository = DocumentRepository()

        document = document_repository.get_document(self.user_id, self.document_id)

        image_bytes: bytes = await download_file(file_id=document.document_id, user_id=self.user_id)

        ext=os.path.splitext(document.document_id)[1][1:]

        result = await validate_document_image_bytes(image_bytes,ext)

        document.valid = (result == "1")
        
        document_repository.update_document(self.user_id,document)
        
        return result


class ValidateDocumentHandler:
    def __init__(self, document_id: str, user_id: str):
        self.document_id = document_id
        self.user_id = user_id

    async def handle(self):
        command = ValidateDocumentCommand(self.document_id, self.user_id)
        return await command.execute()
