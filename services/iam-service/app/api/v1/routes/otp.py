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


