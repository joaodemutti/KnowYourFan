from app.services.google_service import get_esports_content
from app.repositories.user_repository import UserRepository


class GetEsportsQuery:
    def __init__(self,user_id:str):
        self.user_id = user_id
        
    async def execute(self):
        users = UserRepository()
        user = users.get_user(self.user_id)
        return await get_esports_content(user.interests)
    
        
class GetEsportsHandler:
    def __init__(self,user_id):
        self.user_id = user_id

    async def handle(self):
        command = GetEsportsQuery(self.user_id)
        return await command.execute()
