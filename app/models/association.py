from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class UserItem(Base):
    __tablename__ = "user_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    user = relationship("User", back_populates="items_comprados")
    item = relationship("Item", back_populates="users_compraram")

class UserMission(Base):
    __tablename__ = "user_missions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mission_id = Column(Integer, ForeignKey("missions.id"))
    status = Column(String, default='pendente')

    user = relationship("User", back_populates="missions")
    mission = relationship("Mission", back_populates="users")