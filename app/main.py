from fastapi import FastAPI
from app.routers import auth, task, user, item, mission
from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)
app.include_router(item.router)
app.include_router(mission.router)