from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

def get_task(db: Session, task_id: int, user_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id). first()


def get_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
    return db.query(Task).filter(Task.owner_id == user_id).offset(skip).limit(limit).all()


def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
    db_task = Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int, user_id: int) -> bool:
    task = get_task(db, task_id, user_id)
    if task is None:
        return False
    db.delete(task)
    db.commit()
    return True

def update_task(db: Session, task_id: int, user_id: int, task_update: TaskUpdate) -> Optional[Task]:
    task = get_task(db, task_id, user_id)
    if not task:
        return None
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task