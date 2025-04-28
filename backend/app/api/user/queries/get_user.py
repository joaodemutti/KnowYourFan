from app.repositories.user_repository import UserRepository

class GetUserQuery:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def execute(self):
        user_repository = UserRepository()
        user = user_repository.get_user(self.user_id)
        return user

class GetUserHandler:
    def __init__(self, user_id):
        self.user_id = user_id

    def handle(self):
        query = GetUserQuery(self.user_id)
        user = query.execute()
        return user
