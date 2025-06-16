from sqlalchemy.orm import Session
from app.models.mission import Mission
from app.models.association import UserMission
from app.schemas.mission import MissionCreate, MissionProressUpdate, UserMissionCreate, UserMissionResponse

def atualizar_progresso(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()

    if not mission:
        return None
    
    if mission.progresso < 5:
        mission.progresso += 1
    else: mission.progresso = 0

    db.commit()
    db.refresh(mission)
    return mission

def create_mission(db: Session, mission_data: MissionCreate):
    mission = Mission(
        titulo=mission_data.titulo,
        descricao=mission_data.descricao,
        xp_recompensa=mission_data.xp_recompensa,
        coins_recompensa=mission_data.coins_recompensa
    )
    db.add(mission)
    db.commit()
    db.refresh(mission)
    return mission

def assign_mission_to_user(db: Session, user_id: int, user_mission_data: UserMissionCreate):
    user_mission = UserMission(
        user_id=user_id,
        mission_id=user_mission_data.mission_id,
        progresso=0
    )
    db.add(user_mission)
    db.commit()
    db.refresh(user_mission)
    return user_mission