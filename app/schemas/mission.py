from pydantic import BaseModel

class MissionBase(BaseModel):
    titulo: str
    descricao: str | None = None
    xp_recompensa: int
    coins_recompensa: int
    progresso: int

class MissionCreate(MissionBase):
    pass

class UserMissionCreate(BaseModel):
    mission_id: int


class Mission(MissionBase):
    id: int
    user_id: int
    progresso: int

    class Config:
        orm_mode = True