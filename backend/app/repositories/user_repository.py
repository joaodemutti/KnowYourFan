from firebase_admin import firestore
from app.models.user_model import UserCreateDTO, UserDTO
from app.firebase_config import db

class UserRepository:
    def __init__(self):
        self.collection = db.collection("users")

    def create_user(self, user_data: UserCreateDTO):
        _,doc_ref = self.collection.add(user_data.dict())
        return doc_ref.id

    def get_user(self, user_id: str):
        user_ref = self.collection.document(user_id)
        user = user_ref.get()
        if user.exists:
            return user.to_dict()
        return None

    def get_users(self):
        users = []
        docs = self.collection.stream()  # busca todos os documentos
        for doc in docs:
            user_dict = doc.to_dict()
            user_dict["id"] = doc.id  # adiciona o ID do Firebase
            users.append(UserDTO(**user_dict))
        return users