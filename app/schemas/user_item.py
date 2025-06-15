from pydantic import BaseModel
from typing import List

class UserItemCreate(BaseModel):
    item_id: int