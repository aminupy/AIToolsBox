from functools import lru_cache
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from loguru import logger

from app.services import otp_service_provider


class OTPController:
    def __init__(self, otp_service: Annotated[otp_service_provider, Depends()]):
        self.otp_service = otp_service

    async def send_otp(self, email: str):
        logger.info(f"Sending OTP to {email}")
        return await self.otp_service.send_otp(email)

    async def verify_otp(self, email: str, otp: str):
        logger.info(f"Verifying OTP for {email}")
        return await self.otp_service.verify_otp(email, otp)

