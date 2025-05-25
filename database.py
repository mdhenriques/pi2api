from databases import Database

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/pi2-banco"

database = Database(DATABASE_URL)