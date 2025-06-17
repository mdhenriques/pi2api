from pydantic import BaseModel
from datetime import datetime

class NotificationOut(BaseModel):
    id: int
    message: str
    created_at: datetime
    is_read: bool

    class Config:
        orm_mode = True