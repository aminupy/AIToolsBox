import random
from typing import Annotated

from fastapi import Depends
from redis import Redis

from app.core.redis.redis_client import get_redis_client
from app.services.base_service import BaseService


class OTPService(BaseService):
    def __init__(
        self, redis_client: Annotated[Redis, Depends(get_redis_client)]
    ) -> None:
        super().__init__()
        self.redis_client = redis_client

    @staticmethod
    def __generate_otp() -> str:
        return str(random.randint(100000, 999999))

    def send_otp(self, mobile_number: str):
        otp = self.__generate_otp()
        self.redis_client.setex(mobile_number, self.config.OTP_EXPIRE_TIME, otp)
        print(f"OTP sent to {mobile_number}: {otp}")
        return otp

    def verify_otp(self, mobile_number: str, otp: str) -> bool:
        stored_otp = self.redis_client.get(mobile_number)
        return stored_otp is not None and stored_otp == otp
