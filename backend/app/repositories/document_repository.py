from firebase_admin import firestore
from app.models.document_model import DocumentDTO
from app.firebase_config import db

class DocumentRepository:
    def __init__(self):
        self.collection = db.collection("documents")

    def upload_document(self, document_data: DocumentDTO):
        _,doc_ref = self.collection.add(document_data.dict())
        return doc_ref.id

    def validate_document(self, document_id: str):
        document_ref = self.collection.document(document_id)
        document = document_ref.get()
        if document.exists:
            return document.to_dict()
        return None
