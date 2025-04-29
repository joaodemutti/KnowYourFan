from firebase_admin import firestore
from app.models.document_model import Document
from app.config.firebase_config import db

class DocumentRepository:
    def __init__(self):
        self.collection = db.collection("users")

    def create_document(self, user_id: str, document_data: Document):
        user_ref = self.collection.document(user_id)
        user_doc = user_ref.get()

        if not user_doc.exists:
            raise ValueError("Usuário não encontrado.")
        
        doc_data = document_data.model_dump()

        documents_ref = user_ref.collection("documents")
        documents = documents_ref.add(doc_data)

        return documents[1].id

    def get_document(self, user_id:str, document_id: str) -> Document:
        user_ref = self.collection.document(user_id)
        user_doc = user_ref.get()
        
        if not user_doc.exists:
            raise ValueError("Usuário não encontrado.")

        document_ref = user_ref.collection("documents").document(document_id)

        document = document_ref.get()
        
        if document.exists:
            return (Document(**document.to_dict(),id=document.id))
        raise ValueError("Documento não encontrado.")

    def get_documents(self,user_id:str) -> list[Document]:
        user_ref = self.collection.document(user_id)
        user_doc = user_ref.get()
        
        if not user_doc.exists:
            raise ValueError("Usuário não encontrado.")

        documents_collection = user_ref.collection("documents")
        docs = documents_collection.stream()

        documents = []

        for doc in docs:
            doc_dict = doc.to_dict()
            doc_dict["id"] = doc.id
            documents.append(Document(**doc_dict))
        return documents