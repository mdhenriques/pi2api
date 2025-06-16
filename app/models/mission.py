from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Mission(Base):
        __tablename__ = "missions"

        id = Column(Integer, primary_key=True)
        titulo = Column(String, nullable=False)
        descricao = Column(String)
        xp_recompensa = Column(Integer, nullable=False)
        coins_recompensa = Column(Integer, nullable=False)
        # Relacionamentos
        users = relationship('UserMission', back_populates='mission', cascade="all, delete-orphan")
