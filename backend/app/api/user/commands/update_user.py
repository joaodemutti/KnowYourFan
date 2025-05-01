from app.repositories.user_repository import UserRepository
from app.models.user_model import UserUpdateRequest,User
from passlib.hash import bcrypt
from fastapi import HTTPException,status

class UpdateUserCommand:
    def __init__(self, user_data: UserUpdateRequest,user_id:str):
        self.user_data = user_data
        self.user_id = user_id
        if(self.user_data.password):
            self.user_data.password = bcrypt.hash(self.user.password)
        
    def execute(self):
        users = UserRepository()
        user = users.get_user(self.user_id)
        if(user):
            updated_user = user.model_copy(update=self.user_data.model_dump(exclude_none=True))
            users.update_user(updated_user)
            return updated_user
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuário não encontrado.")
        

class UpdateUserHandler:
    def __init__(self, user_data,user_id):
        self.user_data = user_data
        self.user_id = user_id

    def handle(self):
        command = UpdateUserCommand(self.user_data,self.user_id)
        return command.execute()
        