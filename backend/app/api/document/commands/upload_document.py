from app.repositories.document_repository import DocumentRepository
from app.models.document_model import DocumentUploadRequest,Document
from app.services.storage_service import upload_file

class UploadDocumentCommand:
    def __init__(self,user_id:str, document_data: DocumentUploadRequest,):
        self.document_data = document_data
        self.user_id = user_id

    async def execute(self):
        document_repository = DocumentRepository()

        file_id = await upload_file(file=self.document_data.file,user_id=self.user_id)

        document = Document(**self.document_data.model_dump(exclude={"file"}),document_id=file_id)

        document_id = document_repository.create_document(self.user_id,document)
        return document_id
        
class UploadDocumentHandler:
    def __init__(self,user_id, document_data):
        self.document_data = document_data
        self.user_id = user_id

    async def handle(self):
        command = UploadDocumentCommand(self.user_id,self.document_data)
        document_id = await command.execute()
        return document_id
