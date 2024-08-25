from app.core.exceptions import (
    UserAlreadyExistsException,
    OTPServiceException,
    UserNotFoundException,
    UserStatusException
)
from app.core.security import Hasher
from app.domain.models.user_status import UserStatus
from app.domain.schemas.user import (
    UserInitialSignUp,
    UserFinalSignUp
)
from app.domain.schemas.otp import OTPVerify, OTPResponse
from app.services import OTPService
from app.services.base_service import BaseService
from app.services.user_service import UserService
from typing import Annotated
from fastapi import Depends
from loguru import logger


class SignUpService(BaseService):
    def __init__(
        self,
        hash_service: Annotated[Hasher, Depends()],
        user_service: Annotated[UserService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
    ) -> None:
        super().__init__()
        self.user_service = user_service
        self.hash_service = hash_service
        self.otp_service = otp_service

    async def initialize_signup(self, user: UserInitialSignUp) -> OTPResponse:
        existing_user = await self.user_service.get_user_by_email(user.email)
        if existing_user:
            logger.error(f"An account with email {user.email} already exists")
            raise UserAlreadyExistsException(user.email)

        new_user = await self.user_service.initialize_user(user)
        logger.info(f"User with email {user.email} created successfully")

        # Handle OTP service errors locally
        try:
            await self.otp_service.send_otp(new_user.email)
        except OTPServiceException as e:
            logger.error(f"Failed to send OTP: {str(e)}")
            raise OTPServiceException("Failed to send OTP")  # Raising specific exceptions

        return OTPResponse(
            email=user.email,
            expire_time=self.config.OTP_EXPIRE_SECONDS,
            message="User created successfully, OTP sent to email",
        )

    async def verify_signup(self, otp_verify: OTPVerify) -> dict:
        is_verified = await self.otp_service.verify_otp(otp_verify.email, otp_verify.otp)
        if not is_verified:
            logger.error(f"Invalid OTP for email {otp_verify.email}")
            raise OTPServiceException("Invalid OTP")

        user = await self.user_service.get_user_by_email(otp_verify.email)
        if not user:
            logger.error(f"No account with email {otp_verify.email} found")
            raise UserNotFoundException(otp_verify.email)

        await self.user_service.update_user(user.id, {"status": UserStatus.PENDING})
        logger.info(f"User with email {otp_verify.email} verified")
        return {"message": "User verified successfully"}

    async def finalize_signup(self, signup_user: UserFinalSignUp):
        db_user = await self.user_service.get_user_by_email(signup_user.email)
        if not db_user:
            logger.error(f"No account with email {signup_user.email} found")
            raise UserNotFoundException(signup_user.email)

        if db_user.status != UserStatus.PENDING:
            logger.error(f"User with email {db_user.email} is not in sign up state")
            raise UserStatusException(db_user.status)

        await self.user_service.finalize_user(user_id=db_user.id, final_user=signup_user)
        logger.info(f"User with email {db_user.email} signed up successfully")
        return True
