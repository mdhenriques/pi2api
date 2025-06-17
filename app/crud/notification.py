from sqlalchemy.orm import Session
from app.models.notification import Notification

def get_unread_notifications(db: Session, user_id: int):
    return db.query(Notification).filter(
        Notification.user_id == user_id,
        Notification.is_read == False
    ).all()