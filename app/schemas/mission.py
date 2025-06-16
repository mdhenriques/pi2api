from pydantic import BaseModel

class MissionProressUpdate(BaseModel):
    message: str
    novo_progresso: int

class MissionCreate(BaseModel):
    titulo: str
    descricao: str | None = None
    xp_recompensa: int
    coins_recompensa: int

class UserMissionCreate(BaseModel):
    mission_id: int

class UserMissionResponse(BaseModel):
    id: int
    user_id: int
    mission_id: int
    progresso: int

    class Config:
        orm_mode = True