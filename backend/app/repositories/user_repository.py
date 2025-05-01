from firebase_admin import firestore
from app.models.user_model import UserCreateRequest, User
from app.config.firebase_config import db
from fastapi import HTTPException,status

class UserRepository:
    def __init__(self):
        self.collection = db.collection("users")

    def create_user(self, user_data: User):
        _,doc_ref = self.collection.add(user_data.model_dump(exclude={"id"},exclude_none=True))
        return doc_ref.id
    
    def update_user(self, user_data: User):
        self.collection.document(user_data.id).update(user_data.model_dump(exclude={"id"},exclude_none=True))
        return None

    def get_user(self, user_id: str):
        user_ref = self.collection.document(user_id)
        user = user_ref.get()
        if user.exists:
            dict = user.to_dict()
            dict["id"] = user.id
            return User(**dict)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuário não encontrado.")

    def get_user_by_email(self, email: str):
        query = self.collection.where('email', '==', email).limit(1).stream()

        user = None
        for doc in query:
            user = doc.to_dict()
            user["id"] = doc.id
            break

        return user
    
    def get_user_by_facebook(self, facebook: str):
        query = self.collection.where('facebook', '==', facebook).limit(1).stream()

        user = None
        for doc in query:
            user = doc.to_dict()
            user["id"] = doc.id
            return User(**user)
        
        return None
    
    def get_users(self):
        users = []
        docs = self.collection.stream()  # busca todos os documentos
        for doc in docs:
            user_dict = doc.to_dict()
            user_dict["id"] = doc.id  # adiciona o ID do Firebase
            users.append(User(**user_dict))
        return users