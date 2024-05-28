import redis
from app.core.config import get_settings

config = get_settings()

redis_client = redis.StrictRedis.from_url(config.REDIS_URL)


def get_redis_client():
    return redis_client
