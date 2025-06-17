from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Mission(Base):
        __tablename__ = "missions"

        id = Column(Integer, primary_key=True)
        titulo = Column(String, nullable=False)
        descricao = Column(String)
        xp_recompensa = Column(Integer, nullable=False)
        coins_recompensa = Column(Integer, nullable=False)

        user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        progresso = Column(Integer, default=0, nullable=False)
        # Relacionamentos
        user = relationship("User", back_populates="missions")

