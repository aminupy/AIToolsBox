import random
import hashlib
from typing import Annotated
from fastapi import Depends


from app.core.redis.redis_client import get_redis_client
from redis import Redis
from app.core.config import get_settings, Settings


class AuthService:
    def __init__(self,
                 redis_client: Annotated[Redis, Depends(get_redis_client)],
                 config: Annotated[Settings, Depends(get_settings)]
                 ) -> None:
        self.redis_client = redis_client
        self.config = config

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_otp(self) -> str:
        return str(random.randint(100000, 999999))

    def send_otp(self, mobile_number: str):
        otp = self.generate_otp()
        self.redis_client.setex(mobile_number, self.config.OTP_EXPIRE_TIME, otp)
        print(f"OTP sent to {mobile_number}: {otp}")

