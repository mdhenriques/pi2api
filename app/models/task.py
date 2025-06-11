from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.database import Base

class TaskStatus(str, PyEnum):
    PENDENTE = "pendente"
    ANDAMENTO = "andamento"
    CONCLUIDA = "concluida"
    ATRASADA = "atrasada"
    URGENTE = "urgente"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    prazo_entrega = Column(DateTime, nullable=True)
    tempo_estimado = Column(Float, nullable=True)  # Tempo em horas
    repetitiva = Column(Boolean, default=False)
    status = Column(Enum(TaskStatus, name="taskstatus", native_enum=False), default=TaskStatus.PENDENTE)

    user = relationship("User", back_populates="tasks")