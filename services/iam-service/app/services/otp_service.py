import random
from typing import Annotated
from loguru import logger
# importing lru cache
from functools import lru_cache
from fastapi import Depends, HTTPException
from redis import Redis

from app.core.otp import OTPGenerator, OTPVerifier

from app.services.base_service import BaseService


class OTPService(BaseService):

    def __init__(self):
        super().__init__()
        self.generator = OTPGenerator()
        self.verifier = OTPVerifier()

    async def send_otp(self, email: str):
        otp = await self.generator.generate(email)
        logger.info(f"OTP {otp} sent to {email}")
        return True

    async def verify_otp(self, email: str, otp: str) -> bool:
        return await self.verifier.verify(user_identifier=email, otp=otp)


@lru_cache
@logger.catch
def otp_service_provider() -> OTPService:
    return OTPService()
