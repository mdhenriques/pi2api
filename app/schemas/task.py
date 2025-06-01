from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    PENDENTE = "pendente"
    ANDAMENTO = "andamento"
    CONCLUIDA = "concluida"
    ATRASADA = "atrasada"
    URGENTE = "urgente"


class TaskBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prazo_entrega: Optional[datetime] = None
    tempo_estimado: Optional[float] = None
    repetitiva: Optional[bool] = False
    status: Optional[TaskStatus] = TaskStatus.PENDENTE


class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    prazo_entrega: Optional[datetime] = None
    tempo_estimado: Optional[float] = None
    repetitiva: Optional[bool] = None
    status: Optional[TaskStatus] = None


class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True