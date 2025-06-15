from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.database import Base

class ItemType(PyEnum):
    avatar = "avatar"
    background = "background"

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    tipo = Column(Enum(ItemType), nullable=False)
    url = Column(String, nullable=False)    
    preco_coins = Column(Integer, nullable=False)
    preco_xp = Column(Integer, nullable=False)
    

