from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.auth import get_current_user
from app.schemas.user import UpdateUserRewards, EquipAvatar, EquipBackground
from app.schemas.user_item import UserItemCreate, UserItemResponse
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

@router.get("/items", response_model=UserItemResponse)
def get_user_items(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = crud_user.get_user_items(db, current_user.id)
    return {"item_ids": items}

@router.put("/equip/avatar")
def equip_avatar(
    avatar_data: EquipAvatar,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = crud_user.update_avatar(db, current_user.id, avatar_data.avatar_equipado_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Avatar equipado com sucesso", "avatar_id": user.avatar_equipado_id}

@router.put("/equip/background")
def equip_background(
    background_data: EquipBackground,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = crud_user.update_background(db, current_user.id, background_data.background_equipado_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Background equipado com sucesso", "avatar_id": user.background_equipado_id}