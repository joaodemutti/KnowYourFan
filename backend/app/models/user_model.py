from pydantic import BaseModel
from typing import List, Optional

class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str
    address: str
    cpf: str
    interests: List[str]
    activities_last_year: List[str]
    purchases_last_year: List[str]

class User(BaseModel):
    id: str
    email: str
    password: str
    name: str
    address: str
    cpf: str
    interests: List[str]
    activities_last_year: List[str]
    purchases_last_year: List[str]

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    address: str
    cpf: str

class UserDetailResponse(BaseModel):
    id: str
    email: str
    name: str
    address: str
    cpf: str
    interests: List[str]
    activities_last_year: List[str]
    purchases_last_year: List[str]


