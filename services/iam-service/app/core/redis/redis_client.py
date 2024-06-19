from redis import Redis
from loguru import logger

from app.core.config import get_settings

config = get_settings()

try:
    redis_client = Redis(
        host=config.REDIS_URL,
        port=6379,
        charset="utf-8",
        decode_responses=True
    )
    logger.info("Redis Client Created")

except Exception as e:
    logger.error(f"Redis Client Creation Failed: {e}")
    redis_client = None


@logger.catch
def get_redis_client():
    return redis_client
