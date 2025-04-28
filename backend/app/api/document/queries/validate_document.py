from app.repositories.document_repository import DocumentRepository

class ValidateDocumentQuery:
    def __init__(self, document_id: str):
        self.document_id = document_id

    def execute(self):
        document_repository = DocumentRepository()
        document = document_repository.validate_document(self.document_id)
        return document

class ValidateDocumentHandler:
    def __init__(self, document_id):
        self.document_id = document_id

    def handle(self):
        query = ValidateDocumentQuery(self.document_id)
        document = query.execute()
        return document
