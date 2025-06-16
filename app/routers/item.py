from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.item import ItemSchema, ItemCreate
from app.crud import item as item_crud
from app.database import get_db

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

@router.get("/", response_model=List[ItemSchema])
def listar_todos_os_itens(db: Session = Depends(get_db)):
    itens = item_crud.get_all_items(db)
    return itens

@router.post("/", response_model=ItemSchema, status_code=201)
def criar_item(item: ItemCreate, db: Session = Depends(get_db)):
    novo_item = item_crud.create_item(db, item)
    return novo_item