from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.auth import get_current_user
from app.models.user import User
from app.crud import mission as mission_crud
from app.schemas import mission as mission_schema
from typing import List

router = APIRouter(prefix="/mission", tags=["Missions"])



@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_mission(
    mission: mission_schema.MissionCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    new_mission = mission_crud.create_mission(db, mission, current_user.id)
    return {"message": "Missão criada com sucesso", "mission_id": new_mission.id}

@router.get("/", response_model=List[mission_schema.Mission])
def read_missions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return mission_crud.get_missions(db, user_id=current_user.id, skip=skip, limit=limit)

@router.post("/progresso/{mission_id}", response_model=mission_schema.Mission)
def increment_progress(
    mission_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        updated_mission = mission_crud.increment_user_mission_progress(db, current_user.id, mission_id)
        return updated_mission
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))