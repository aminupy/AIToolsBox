from redis import Redis
from app.core.config import get_settings

config = get_settings()

redis_client = Redis(
    host=config.REDIS_URL,
    port=6379,
    charset="utf-8",
    decode_responses=True
)


def get_redis_client():
    return redis_client
