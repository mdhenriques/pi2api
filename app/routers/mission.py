from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.mission import MissionProressUpdate, MissionCreate, UserMissionResponse, UserMissionCreate
from app.crud import mission as mission_crud

router = APIRouter(prefix="/mission", tags=["Missions"])

@router.put("/{mission_id}/progresso", response_model=MissionProressUpdate)
def update_mission_progress(mission_id: int, db: Session = Depends(get_db)):
    mission = mission_crud.atualizar_progresso(db, mission_id)

    if not mission:
        raise HTTPException(status_code=404, detail="Missão não encontrada")
    
    return MissionProressUpdate(
        message=f"Progresso da missão {mission_id} atualizado com sucesso",
        novo_progresso=mission.progresso
    )

@router.post("/", response_model=dict)
def create_mission(mission: MissionCreate, db: Session = Depends(get_db)):
    new_mission = mission_crud.create_mission(db, mission)
    return {"message": "Missão criada com sucesso", "mission_id": new_mission.id}

@router.post("/assign/{user_id}", response_model=UserMissionResponse)
def assign_mission(user_id: int, user_mission: UserMissionCreate, db: Session = Depends(get_db)):
    assigned = mission_crud.assign_mission_to_user(db, user_id, user_mission)
    return assigned