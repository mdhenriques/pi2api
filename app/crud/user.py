from sqlalchemy.orm import Session, relationship
from app.models.user import User
from app.schemas.user import UserCreate, UpdateUserRewards
from passlib.context import CryptContext
from app.utils.auth import get_password_hash

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
