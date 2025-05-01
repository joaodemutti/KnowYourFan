from fastapi import APIRouter
from app.services.auth_service import login_user,facebook_user
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class FacebookRequest(BaseModel):
    access_token: str

@router.post("/login")
def login(credentials:LoginRequest):
    return login_user(credentials.email, credentials.password)

@router.post("/facebook")
def facebook(credentials:FacebookRequest):
    return facebook_user(credentials.access_token)
