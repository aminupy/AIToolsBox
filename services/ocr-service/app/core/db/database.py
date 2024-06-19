from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import get_settings
from loguru import logger

try:
    config = get_settings()
    client = AsyncIOMotorClient(config.DATABASE_URL)
    db = client[config.DATABASE_NAME]
    logger.info("MongoDB Database connected")

except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
    raise e


async def get_db():
    yield db
