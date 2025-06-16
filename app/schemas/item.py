from pydantic import BaseModel
from enum import Enum

class ItemType(str, Enum):
    avatar = "avatar"
    background = "background"

class ItemSchema(BaseModel):
    id: int
    nome: str
    descricao: str | None
    tipo: ItemType
    url: str
    preco_coins: int
    preco_xp: int

    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    nome: str
    descricao: str | None
    tipo: ItemType
    url: str
    preco_coins: int
    preco_xp: int

class ItemSchema(ItemCreate):
    id: int

    class Config:
        orm_mode = True