from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, task, user, item, mission, notification
from app.database import Base, engine
from app.scheduler.notification_jobs import check_task_deadlines
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Inicialize o scheduler antes
scheduler = BackgroundScheduler()
scheduler.add_job(check_task_deadlines, 'interval', hours=24)

@app.on_event("startup")
def start_scheduler():
    print("Iniciando scheduler...")
    scheduler.start()
    # Forçar rodar o job de teste na primeira inicialização
    check_task_deadlines()

@app.on_event("shutdown")
def shutdown_event():
    print("Encerrando scheduler...")
    scheduler.shutdown()

# Rotas
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)
app.include_router(item.router)
app.include_router(mission.router)
app.include_router(notification.router)
