from app.repositories.user_repository import UserRepository

class GetUsersQuery:
    def execute(self):
        user_repository = UserRepository()
        users = user_repository.get_users()
        return users

class GetUsersHandler:

    def handle(self):
        query = GetUsersQuery()
        users = query.execute()
        return users
