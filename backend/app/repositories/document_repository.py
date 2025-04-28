from firebase_admin import firestore
from app.models.document_model import DocumentDTO
from app.config.firebase_config import db

class DocumentRepository:
    def __init__(self):
        self.collection = db.collection("users")

    def upload_document(self, user_id: str, document_data: DocumentDTO):
        user_ref = self.collection.document(user_id)
        user_doc = user_ref.get()

        if not user_doc.exists:
            raise ValueError("Usuário não encontrado.")
        
        doc_data = document_data.model_dump()

        documents_ref = user_ref.collection("documents")
        documents = documents_ref.add(doc_data)

        return documents[1].id

    def validate_document(self, user_id:str, document_id: str):
        user_ref = self.collection.document(user_id)
        user_doc = user_ref.get()
        
        if not user_doc.exists:
            raise ValueError("Usuário não encontrado.")

        document_ref = user_ref.collection("documents").document(document_id)

        document = document_ref.get()
        
        if document.exists:
            return document.to_dict()
        
        return None

        