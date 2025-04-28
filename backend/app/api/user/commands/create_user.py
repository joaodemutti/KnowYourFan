from app.repositories.user_repository import UserRepository
from app.models.user_model import UserCreateDTO

class CreateUserCommand:
    def __init__(self, user_data: UserCreateDTO):
        self.user_data = user_data

    def execute(self):
        user_repository = UserRepository()
        user_id = user_repository.create_user(self.user_data)
        return user_id

class CreateUserHandler:
    def __init__(self, user_data):
        self.user_data = user_data

    def handle(self):
        command = CreateUserCommand(self.user_data)
        user_id = command.execute()
        return user_id