from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models.task import Task
from app.models.notification import Notification

def check_task_deadlines():
    db: Session = SessionLocal()
    print("job rodando")
    try:
        tomorrow = datetime.now() + timedelta(days=1)

        tasks = db.query(Task).filter(
            Task.prazo_entrega >= datetime.now(),
            Task.prazo_entrega < tomorrow
        ).all()

        for task in tasks:
            notification = Notification(
                user_id=task.user_id,
                message=f"Falta 1 dia para entrega da tarefa '{task.titulo}'"

            )
            db.add(notification)
            db.commit()
    finally:
        db.close()