from pydantic import BaseModel
from typing import List, Optional

class UserCreateDTO(BaseModel):
    name: str
    address: str
    cpf: str
    interests: List[str]
    activities_last_year: List[str]
    purchases_last_year: List[str]

class UserDTO(BaseModel):
    id: str
    name: str
    address: str
    cpf: str
    interests: List[str]
    activities_last_year: List[str]
    purchases_last_year: List[str]


