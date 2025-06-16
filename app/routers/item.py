from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.item import ItemSchema
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