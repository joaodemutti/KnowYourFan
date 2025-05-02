from pydantic import BaseModel, Field
from typing import List, Optional

class UserCreateRequest(BaseModel):
    name: str
    facebook: Optional[str] = None
    email: str
    password: str
    address: Optional[str] = None
    cpf: Optional[str] = None
    interests: Optional[List[str]] = None

class UserUpdateRequest(BaseModel): 
    name: Optional[str] = None
    facebook: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    cpf: Optional[str] = None
    interests: Optional[List[str]] = None

class User(BaseModel):
    id: Optional[str] = Field(default=None, exclude=True)
    facebook: Optional[str] = None
    email: str
    password: Optional[str] = None
    name: str
    address: Optional[str] = None
    cpf: Optional[str] = None
    interests: Optional[List[str]] = None

class UserResponse(BaseModel):
    id: str
    user: bool = True
    email: str
    name: str
    address: Optional[str] = None
    cpf: Optional[str] = None

class UserDetailResponse(BaseModel):
    id: str
    email: str
    name: str
    address: Optional[str] = None
    cpf: Optional[str] = None
    interests: Optional[List[str]] = None


