from datetime import datetime, timedelta, timezone
from typing import Annotated
from loguru import logger
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.exceptions import UserStatusException
from app.domain.models.user import User
from app.domain.models.user_status import UserStatus
from app.domain.schemas.otp import OTPResponse, OTPVerifyRequest, OTPVerifyResponse
from app.domain.schemas.token import Token
from app.domain.schemas.user import UserSignIn, UserInitialSignUp, UserFinalSignUp, UserInitialSignUpResponse
from app.services.otp_service import OTPService
from app.services.user_service import UserService
from app.services.base_service import BaseService
from app.services.sub_services import SignUpService, SignInService
from app.utilites.user_utils import get_existing_user


class AuthService(BaseService):
    def __init__(
        self,
        signup_service: Annotated[SignUpService, Depends()],
        signin_service: Annotated[SignInService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
        user_service: Annotated[UserService, Depends()],
    ) -> None:
        super().__init__()
        self.signup_service = signup_service
        self.signin_service = signin_service
        self.otp_service = otp_service
        self.user_service = user_service

    async def __get_otp_user(self, email: str) -> User:
        user = await get_existing_user(email, self.user_service)
        if user.status == UserStatus.Verified:
            logger.error(f"User {email} is already verified")
            raise UserStatusException(user.status)
        return user

    async def initialize_signup(self, user: UserInitialSignUp) -> UserInitialSignUpResponse:
        return await self.signup_service.initialize_signup(user)

    async def finalize_signup(self, user: UserFinalSignUp) -> Token:
        await self.signup_service.finalize_signup(user)
        return await self.signin_service.signin(UserSignIn(email=user.email, password=user.password))

    async def signin(self, user: UserSignIn) -> Token:
        return await self.signin_service.signin(user)

    async def send_otp(self, email: str) -> OTPResponse:
        await self.__get_otp_user(email)
        expire_time = await self.otp_service.send_otp(email)
        return OTPResponse(
            email=email,
            expire_time=expire_time,
            message="OTP Sent Successfully."
        )

    async def verify_otp(self, otp_verify: OTPVerifyRequest) -> OTPVerifyResponse:
        user = await self.__get_otp_user(otp_verify.email)
        if await self.otp_service.verify_otp(otp_verify.email, otp_verify.otp):
            await self.user_service.update_user_status(user_id=user.id, status="verified")
            return OTPVerifyResponse(
                email=otp_verify.email,
                status=UserStatus.Verified,
                message="User Verified Successfully."
            )




