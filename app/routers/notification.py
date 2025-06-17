from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.user import User
from app.schemas.notifications import NotificationOut
from app.crud import notification as crud_not
from app.models.notification import Notification as model_not
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)

@router.get("/unread", response_model=List[NotificationOut])
def get_unread_notification(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return crud_not.get_unread_notifications(db, current_user.id)