from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    xp: int
    coins: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    senha: str


# Para retorno do token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Para payload do token JWT
class TokenData(BaseModel):
    email: Optional[str] = None