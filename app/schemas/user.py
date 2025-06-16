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
    username: str
    senha: str

class UpdateUserRewards(BaseModel):
    xp: Optional[int] = None
    coins: Optional[int] = None

class EquipAvatar(BaseModel):
    avatar_equipado_id: int

class EquipBackground(BaseModel):
    background_equipado_id: int

# Para retorno do token
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Para payload do token JWT
class TokenData(BaseModel):
    email: Optional[str] = None