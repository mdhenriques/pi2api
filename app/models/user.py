from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from .association import UserItem, UserMission
from .item import Item
from .task import Task
from .mission import Mission

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    xp = Column(Integer, default=0)
    coins = Column(Integer, default=0)

    avatar_equipado_id = Column(Integer, ForeignKey("items.id"), nullable=True)
    background_equipado_id = Column(Integer, ForeignKey("items.id"), nullable=True)

    avatar_equipado = relationship("Item", foreign_keys=[avatar_equipado_id])
    background_equipado = relationship("Item", foreign_keys=[background_equipado_id])

    items_comprados = relationship('UserItem', back_populates='user')
    tasks = relationship('Task', back_populates='user')
    missions = relationship('UserMission', back_populates='user')
