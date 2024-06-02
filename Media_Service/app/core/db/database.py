from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import get_settings

config = get_settings()

client = AsyncIOMotorClient(config.DATABASE_URL)
db = client[config.DATABASE_NAME]


async def get_db():
    yield db
