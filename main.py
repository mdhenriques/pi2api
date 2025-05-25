from fastapi import FastAPI
from database import database
from crud import create_user, get_users

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/")
async def add_user(name: str, email: str):
    user_id = await create_user(name, email)
    return {"id": user_id, "name": name, "email": email}

@app.get("/users/")
async def list_users():
    return await get_users()
