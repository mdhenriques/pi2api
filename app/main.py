from fastapi import FastAPI
from app.routers import auth, task, user
from app.database import Base, engine
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(task.router)
