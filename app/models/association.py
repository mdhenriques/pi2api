from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.postgresql import ARRAY
from app.database import Base

class UserItem(Base):
    __tablename__ = "user_items"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    item_ids = Column(MutableList.as_mutable(ARRAY(Integer)), nullable=False, default=[])

    user = relationship("User", back_populates="items_comprados")

class UserMission(Base):
    __tablename__ = "user_missions"
    __table_args__ = (
        UniqueConstraint('user_id', 'mission_id', name='uix_user_mission'),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mission_id = Column(Integer, ForeignKey("missions.id"), nullable=False)
    progresso = Column(Integer, default=0, nullable=False)

    user = relationship("User", back_populates="missions")
    mission = relationship("Mission", back_populates="users")
