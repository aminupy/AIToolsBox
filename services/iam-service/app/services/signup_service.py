from typing import Annotated
from loguru import logger
from fastapi import Depends, HTTPException, status

from app.domain.models.user_status import UserStatus
from app.domain.schemas.user import (
    UserInitialSignUp,
    UserFinalSignUp
)
from app.domain.schemas.otp import OTPVerify
from app.domain.schemas.otp import OTPResponse
from app.services.auth_service import AuthService
from app.services.otp_service import OTPService
from app.services.base_service import BaseService
from app.services.user_service import UserService


class SignUpService(BaseService):
    def __init__(
            self,
            user_service: Annotated[UserService, Depends()],
            otp_service: Annotated[OTPService, Depends()],
            auth_service: Annotated[AuthService, Depends()],
    ) -> None:
        super().__init__()

        self.user_service = user_service
        self.otp_service = otp_service
        self.auth_service = auth_service

    async def initial_signup(self, user: UserInitialSignUp) -> OTPResponse:
        existing_email = await self.user_service.get_user_by_email(user.email)

        if existing_email:
            logger.error(f"An account with email {user.email} already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )

        new_user = await self.user_service.initialize_user(user)
        logger.info(f"User with email {user.email} created successfully")

        await self.otp_service.send_otp(new_user.email)

        return OTPResponse(
            email=user.email,
            expire_time=self.config.OTP_EXPIRE_SECONDS,
            message="User created successfully, OTP sent to email",
        )

    async def final_signup(self, user: UserFinalSignUp):
        user = await self.user_service.get_user_by_email(user.email)

        if not user:
            logger.error(f"No account with email {user.email} found")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        if user.status == UserStatus.ACTIVE:
            logger.error(f"User with email {user.email} already signed up")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already signed up"
            )

        if user.status == UserStatus.UnVerified:
            logger.error(f"User with email {user.email} not verified")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User not verified"
            )

        if not user.status == UserStatus.PENDING:
            logger.error(f"User with email {user.email} is not in sign up state")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User is not in sign up state"
            )

        await self.user_service.finalize_user(user)

        logger.info(f"User with email {user.email} signed up successfully")
        return {
            "message": "User signed up successfully"
        }

    async def verify_user(
            self, otp_verify: OTPVerify
    ):
        if not self.otp_service.verify_otp(otp_verify.email, otp_verify.otp):
            logger.error(f"Invalid OTP for email {otp_verify.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP"
            )

        user = await self.user_service.get_user_by_email(
            otp_verify.email
        )

        await self.user_service.update_user(user.id, {"status": UserStatus.PENDING})

        logger.info(f"User with email {otp_verify.email} verified")
        return {
            "message": "User verified successfully"
        }

    async def send_otp(
            self, resend_otp_schema: ResendOTPSchema
    ) -> ResendOTPResponseSchema:
        existing_user = await self.user_service.get_user_by_mobile_number(
            resend_otp_schema.mobile_number
        )
        if not existing_user:
            logger.error(f"User with mobile number {resend_otp_schema.mobile_number} does not exist")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )

        if existing_user.is_verified:
            logger.error(f"User with mobile number {resend_otp_schema.mobile_number} already verified")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already verified"
            )

        if self.otp_service.check_exist(resend_otp_schema.mobile_number):
            logger.error(f"OTP for mobile number {resend_otp_schema.mobile_number} already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="OTP already exists"
            )

        otp = self.otp_service.send_otp(resend_otp_schema.mobile_number)

        logger.info(f"OTP resent to mobile number {resend_otp_schema.mobile_number}")
        return ResendOTPResponseSchema(
            mobile_number=resend_otp_schema.mobile_number,
            OTP=otp,
            message="OTP sent to mobile number",
        )
