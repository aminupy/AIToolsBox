from fastapi import Depends, status, APIRouter
from typing import Annotated
from loguru import logger

from app.services.otp_service import OTPService
from app.domain.schemas.otp import (
    OTPRequest,
    OTPResponse,
    OTPVerify,
)

router = APIRouter()


@router.post(
    "/request",
    response_model=OTPResponse,
    status_code=status.HTTP_201_CREATED,
)
async def request_otp(
    otp_request: OTPRequest,
    otp_service: Annotated[OTPService, Depends()]
) -> OTPResponse:
    logger.info(f"Requesting OTP for email {otp_request.email}")
    await otp_service.send_otp(otp_request.email)
    return OTPResponse(
        email=otp_request.email,
        expire_time=otp_service.config.OTP_EXPIRE_SECONDS,
        message="OTP sent successfully"
    )


@router.post(
    "/verify",
    response_model=OTPResponse,
    status_code=status.HTTP_200_OK,
)
async def verify_otp(
    otp_verify: OTPVerify,
    otp_service: Annotated[OTPService, Depends()]
) -> OTPResponse:
    logger.info(f"Verifying OTP for email {otp_verify.email} with OTP {otp_verify.otp}")
    await otp_service.verify_otp(otp_verify.email, otp_verify.otp)
