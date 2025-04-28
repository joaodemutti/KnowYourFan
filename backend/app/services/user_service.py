from app.repositories.user_repository import UserRepository
from app.models.user_model import UserCreateDTO

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user_data: UserCreateDTO):
        return self.user_repository.create_user(user_data)

    def get_user(self, user_id: str):
        return self.user_repository.get_user(user_id)
