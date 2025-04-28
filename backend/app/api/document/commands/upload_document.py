from app.repositories.document_repository import DocumentRepository
from app.models.document_model import DocumentDTO

class UploadDocumentCommand:
    def __init__(self,user_id:str, document_data: DocumentDTO):
        self.document_data = document_data
        self.user_id = user_id

    def execute(self):
        document_repository = DocumentRepository()
        document_id = document_repository.upload_document(self.user_id,self.document_data)
        return document_id
        
class UploadDocumentHandler:
    def __init__(self,user_id, document_data):
        self.document_data = document_data
        self.user_id = user_id

    def handle(self):
        command = UploadDocumentCommand(self.user_id,self.document_data)
        document_id = command.execute()
        return document_id
