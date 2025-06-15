from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.utils.auth import get_current_user
from app.schemas.user import Token, UserCreate, UserLogin, UpdateUserRewards
from app.crud import user as crud_user
from app.database import get_db
from passlib.context import CryptContext

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/me")
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/rewards")
def update_user_rewards(
    rewards: UpdateUserRewards,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    user = crud_user.update_user_rewards(db, current_user.id, rewards)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return {
        "message": "User rewards updated successfully",
        "user": {
            "id": user.id,
            "xp": user.xp,
            "coins": user.coins
        }
    }