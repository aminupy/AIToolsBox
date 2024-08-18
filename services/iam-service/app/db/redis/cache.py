from app.db.redis.client import redis_client


def set_cache(key: str, value: str, expire_time: int):
    redis_client.setex(key, expire_time, value)


def get_cache(key: str):
    return redis_client.get(key)