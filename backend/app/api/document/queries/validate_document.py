from app.repositories.document_repository import DocumentRepository

class ValidateDocumentQuery:
    def __init__(self,user_id, document_id):
        self.document_id = document_id
        self.user_id = user_id

    def execute(self):
        document_repository = DocumentRepository()
        document = document_repository.validate_document(self.user_id,self.document_id)
        return document

class ValidateDocumentHandler:
    def __init__(self,user_id, document_id):
        self.document_id = document_id
        self.user_id = user_id

    def handle(self):
        query = ValidateDocumentQuery(self.user_id,self.document_id)
        document = query.execute()
        return document
