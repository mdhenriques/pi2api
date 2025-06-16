from sqlalchemy.orm import Session
from app.models.item import Item

def get_all_items(db: Session):
    return db.query(Item).all()