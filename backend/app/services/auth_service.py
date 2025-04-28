# app/services/auth_service.py
from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from passlib.hash import bcrypt

# Carrega as variáveis do .env
load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", 60))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def login_user(email: str, password: str):
    user_repo = UserRepository()
    user = user_repo.get_user_by_email(email)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")

    if not bcrypt.verify(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Senha inválida")

    token = create_access_token({"sub": user["id"]})
    return {"access_token": token, "token_type": "bearer"}