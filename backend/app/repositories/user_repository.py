from firebase_admin import firestore
from app.models.user_model import UserCreateRequest, User
from app.config.firebase_config import db

class UserRepository:
    def __init__(self):
        self.collection = db.collection("users")

    def create_user(self, user_data: UserCreateRequest):
        _,doc_ref = self.collection.add(user_data.model_dump())
        return doc_ref.id

    def get_user(self, user_id: str):
        user_ref = self.collection.document(user_id)
        user = user_ref.get()
        if user.exists:
            return User(**user.to_dict())
        raise ValueError("Usuário não encontrado.")

    def get_user_by_email(self, email: str):
        query = self.collection.where('email', '==', email).limit(1).stream()

        user = None
        for doc in query:
            user = doc.to_dict()
            user["id"] = doc.id
            break

        return user
    
    def get_users(self):
        users = []
        docs = self.collection.stream()  # busca todos os documentos
        for doc in docs:
            user_dict = doc.to_dict()
            user_dict["id"] = doc.id  # adiciona o ID do Firebase
            users.append(User(**user_dict))
        return users