from fastapi import APIRouter, HTTPException
from app.api.user.commands.create_user import CreateUserHandler
from app.api.user.queries.get_user import GetUserHandler
from app.api.user.queries.get_users import GetUsersHandler
from app.models.user_model import UserCreateDTO, UserDTO
from typing import List

router = APIRouter()

@router.post("/user", response_model=UserDTO)
async def create_user(user: UserCreateDTO):
    handler = CreateUserHandler(user_data=user)
    user_id = handler.handle()
    return {**user.dict(), "id": user_id}

@router.get("/users",response_model=list[UserDTO])
async def get_users():
    handler = GetUsersHandler()
    users = handler.handle()
    return users

@router.get("/users/{user_id}", response_model=UserDTO)
async def get_user(user_id: str):
    handler = GetUserHandler(user_id=user_id)
    user = handler.handle()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
