from sqlalchemy.orm import Session
from app.models.user import User
from schemas.user import UserCreate
from passlib.context import CryptContext

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