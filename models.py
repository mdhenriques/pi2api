from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from database import DATABASE_URL

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("email", String(100)),
)

# Cria as tabelas no banco (apenas se não existirem)
engine = create_engine(str(DATABASE_URL).replace('+asyncpg', ''))
metadata.create_all(engine)
