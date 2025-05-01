from fastapi import APIRouter, HTTPException, Depends
from app.api.user.commands.create_user import CreateUserHandler
from app.api.user.queries.get_user import GetUserHandler
from app.api.user.queries.get_users import GetUsersHandler
from app.api.user.commands.update_user import UpdateUserHandler 
from app.models.user_model import UserCreateRequest, UserResponse, UserDetailResponse, UserUpdateRequest
from typing import List
from app.api.auth.dependency import get_current_user

router = APIRouter()

@router.get("/me",response_model=UserDetailResponse)
async def me(user_id: str =  Depends(get_current_user)):
    handler = GetUserHandler(user_id=user_id)
    user = handler.handle()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
async def create_user(user: UserCreateRequest):
    handler = CreateUserHandler(user_data=user)
    user_id = handler.handle()
    return { "id": user_id}

@router.put("/users",response_model=UserDetailResponse)
async def update_user(user:UserUpdateRequest, user_id: str =  Depends(get_current_user)):
    handler = UpdateUserHandler(user_data=user,user_id=user_id)
    user = handler.handle()
    return user

# @router.get("/users",response_model=list[UserResponse])
# async def get_users():
#     handler = GetUsersHandler()
#     users = handler.handle()
#     return users

# @router.get("/users/{user_id}", response_model=UserDetailResponse)
# async def get_user(user_id: str):
#     handler = GetUserHandler(user_id=user_id)
#     user = handler.handle()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

