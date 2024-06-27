from typing import Annotated
from loguru import logger
from fastapi import Depends, HTTPException, status

from app.domain.schemas.user_schema import (
    UserCreateSchema,
    UserSchema,
    UserCreateResponseSchema,
    VerifyOTPSchema,
    VerifyOTPResponseSchema,
    ResendOTPSchema,
    ResendOTPResponseSchema,
)
from app.services.auth_services.auth_service import AuthService
from app.services.auth_services.otp_service import OTPService
from app.services.base_service import BaseService
from app.services.user_service import UserService


class RegisterService(BaseService):
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

    async def register_user(self, user: UserCreateSchema) -> UserCreateResponseSchema:
        existing_mobile_number = await self.user_service.get_user_by_mobile_number(
            user.mobile_number
        )

        if existing_mobile_number:
            logger.error(f"User with mobile number {user.mobile_number} already exists")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists"
            )

        new_user = await self.user_service.create_user(user)
        otp = self.otp_service.send_otp(new_user.mobile_number)

        logger.info(f"User with mobile number {user.mobile_number} created successfully")
        return UserCreateResponseSchema(
            user=UserSchema.from_orm(new_user),
            OTP=otp,
            message="User created successfully, OTP sent to mobile number",
        )

    async def verify_user(
        self, verify_user_schema: VerifyOTPSchema
    ) -> VerifyOTPResponseSchema:
        if not self.otp_service.verify_otp(
            verify_user_schema.mobile_number, verify_user_schema.OTP
        ):
            logger.error(f"Invalid OTP for mobile number {verify_user_schema.mobile_number}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP"
            )

        user = await self.user_service.get_user_by_mobile_number(
            verify_user_schema.mobile_number
        )

        await self.user_service.update_user(user.id, {"is_verified": True})

        logger.info(f"User with mobile number {verify_user_schema.mobile_number} verified")
        return VerifyOTPResponseSchema(
            verified=True, message="User verified successfully"
        )

    async def resend_otp(
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
