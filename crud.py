from database import database
from models import users

async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    return await database.execute(query)

async def get_users():
    query = users.select()
    return await database.fetch_all(query)
