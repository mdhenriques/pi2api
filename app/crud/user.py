from sqlalchemy.orm import Session, relationship
from app.models.association import UserItem
from app.models.user import User
from app.models.item import Item
from app.schemas.user import UserCreate, UpdateUserRewards
from passlib.context import CryptContext
from app.utils.auth import get_password_hash
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username= user.username,
        email=user.email,
        password_hash=get_password_hash(user.password),
    )
    db.Add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_rewards(db: Session, user_id: int, rewards: UpdateUserRewards):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    if rewards.xp is not None:
        user.xp += rewards.xp

    if rewards.coins is not None:
        user.coins += rewards.coins

    db.commit()
    db.refresh(user)

    return user

tasks = relationship("Task", back_populates="user")


def create_user_item(db: Session, user_id: int, item_id: int):
    # Primeiro busca o registro de UserItem do usuário
    user_items = db.query(UserItem).filter(UserItem.user_id == user_id).first()

    # Se o usuário já tem um registro de items
    if user_items:
        # Caso o campo venha como None
        if user_items.item_ids is None:
            user_items.item_ids = []

        # Se o item já estiver no array, bloqueia
        if item_id in user_items.item_ids:
            raise HTTPException(status_code=400, detail="Usuário já possui este item")

        # Adiciona o novo item ao array
        print(user_items.item_ids)
        user_items.item_ids.append(item_id)
        print(user_items.item_ids)


    else:
        # Se for o primeiro item do usuário, cria o registro
        user_items = UserItem(user_id=user_id, item_ids=[item_id])
        db.add(user_items)

    db.commit()
    db.refresh(user_items)

    return user_items

def get_user_items(db: Session, user_id: int):
    user_items = db.query(UserItem).filter(UserItem.user_id == user_id).first()
    if user_items:
        return user_items.item_ids
    return []

def update_avatar(db: Session, user_id: int, avatar_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.avatar_equipado_id = avatar_id
    item = db.query(Item).filter(Item.id == user.avatar_equipado_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado.")

    db.commit()
    db.refresh(user)
    return user

def update_background(db: Session, user_id: int, background_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.background_equipado_id = background_id
    item = db.query(Item).filter(Item.id == user.background_equipado_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado.")

    db.commit()
    db.refresh(user)
    return user



