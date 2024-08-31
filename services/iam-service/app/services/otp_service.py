from typing import Annotated
from fastapi import Depends
from loguru import logger

from app.core.otp import OTPGenerator, OTPVerifier
from app.core.exceptions import OTPServiceException


class OTPService:

    def __init__(
        self,
        generator: Annotated[OTPGenerator, Depends()],
        verifier: Annotated[OTPVerifier, Depends()],
    ):
        super().__init__()
        self.generator = generator
        self.verifier = verifier

    async def send_otp(self, email: str):
        try:
            otp, expire_time = await self.generator.generate(email)
            logger.info(f"OTP {otp} sent to {email}")

            return expire_time
        except Exception as e:
            logger.error(f"Failed to send OTP to {email}: {e}")
            raise OTPServiceException(f"Failed to send OTP to {email}")

    async def verify_otp(self, email: str, otp: str) -> True:
        if not await self.verifier.verify(user_identifier=email, otp=otp):
            raise OTPServiceException(f"Invalid OTP for {email}")
        else:
            return True
