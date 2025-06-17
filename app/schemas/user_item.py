from pydantic import BaseModel
from typing import List

class UserItemCreate(BaseModel):
    item_id: int

class UserItemResponse(BaseModel):
    item_ids: List[int]

    class Config:
        orm_mode = True