from app.repositories.document_repository import DocumentRepository
from app.models.document_model import DocumentDTO

class DocumentService:
    def __init__(self):
        self.document_repository = DocumentRepository()

    def upload_document(self, document_data: DocumentDTO):
        return self.document_repository.upload_document(document_data)

    def validate_document(self, document_id: str):
        return self.document_repository.validate_document(document_id)
