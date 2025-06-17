from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import task as task_schema
from app.crud import task as task_crud
from app.database import get_db
from app.utils.auth import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post("/", response_model=task_schema.Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task: task_schema.TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_crud.create_task(db, task, user_id=current_user.id)

@router.get("/", response_model=List[task_schema.Task])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return task_crud.get_tasks(db, user_id=current_user.id, skip=skip, limit=limit)

@router.get("/{task_id}", response_model=task_schema.Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = task_crud.get_task(db, task_id, user_id=current_user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=task_schema.Task)
def update_task(
    task_id: int,
    task_update: task_schema.TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = task_crud.update_task(db, task_id, current_user.id, task_update)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    success = task_crud.delete_task(db, task_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
