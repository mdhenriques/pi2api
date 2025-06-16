from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate

def get_all_items(db: Session):
    return db.query(Item).all()

def create_item(db: Session, item: ItemCreate):
    db_item = Item(
        nome=item.nome,
        descricao=item.descricao,
        tipo=item.tipo,
        url=item.url,
        preco_coins=item.preco_coins,
        preco_xp=item.preco_xp
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item