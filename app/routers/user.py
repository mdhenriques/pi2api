from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.association import UserItem
from app.utils.auth import get_current_user
from app.schemas.user import UpdateUserRewards
from app.schemas.user_item import UserItemCreate
from app.crud import user as crud_user
from app.database import get_db


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

@router.post("/buy")
def add_items_to_user(
    user_item_data: UserItemCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = crud_user.create_user_item(db, current_user.id, user_item_data.item_id)
    return {
        "message": "Item adicionado com sucesso",
        "user_items": result.item_ids
    }