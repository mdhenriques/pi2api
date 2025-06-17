from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.mission import Mission as MissionModel
from app.schemas.mission import MissionCreate

def get_missions(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[MissionModel]:
    return db.query(MissionModel).filter(MissionModel.user_id == user_id).offset(skip).limit(limit).all()

def create_mission(db: Session, mission: MissionCreate, user_id: int):
    db_mission = MissionModel(**mission.model_dump(), user_id=user_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission

def increment_user_mission_progress(db: Session, user_id: int, mission_id = int):
    mission = db.query(MissionModel).filter(
        MissionModel.id == mission_id,
        MissionModel.user_id == user_id
    ).first()

    if not mission:
        raise ValueError(f"Missão id={mission_id} não pertence ao usuário")
    
    mission.progresso = (mission.progresso + 1) % 6

    db.commit()
    db.refresh(mission)
    return mission