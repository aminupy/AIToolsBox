from typing import Annotated
from loguru import logger
from functools import lru_cache
from fastapi import Depends

from app.core.otp import OTPGenerator, OTPVerifier
from app.core.exceptions import OTPServiceException
from app.services.base_service import BaseService


class OTPService(BaseService):

    def __init__(
            self,
            generator: Annotated[OTPGenerator, Depends()],
            verifier: Annotated[OTPVerifier, Depends()]
            ):
        super().__init__()
        self.generator = generator
        self.verifier = verifier

    async def send_otp(self, email: str):
        try:
            otp = await self.generator.generate(email)
            logger.info(f"OTP {otp} sent to {email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send OTP to {email}: {e}")
            raise OTPServiceException(f"Failed to send OTP to {email}")

    async def verify_otp(self, email: str, otp: str) -> bool:
        try:
            return await self.verifier.verify(user_identifier=email, otp=otp)
        except Exception as e:
            logger.error(f"Failed to verify OTP for {email}: {e}")
            raise OTPServiceException(f"Failed to verify OTP for {email}")


@lru_cache
@logger.catch
def otp_service_provider() -> OTPService:
    return OTPService()

