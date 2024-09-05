from typing import Annotated
from loguru import logger
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestFormStrict

from app.core.exceptions import UserStatusException, InvalidGrantTypeException
from app.domain.models.user import User
from app.domain.models.user_status import UserStatus
from app.domain.schemas.otp import OTPResponse, OTPVerifyRequest, OTPVerifyResponse
from app.domain.schemas.token import Token
from app.domain.schemas.user import UserSignIn
from app.services.otp_service import OTPService
from app.services.user_service import UserService
from app.services.signin_service import SignInService
from app.core.security import TokenManager
from app.utils.user_utils import get_existing_user


class AuthService:
    def __init__(
        self,
        signin_service: Annotated[SignInService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
        user_service: Annotated[UserService, Depends()],
        token_manager: Annotated[TokenManager, Depends()],
    ) -> None:
        super().__init__()
        self.signin_service = signin_service
        self.otp_service = otp_service
        self.user_service = user_service
        self.token_manager = token_manager

    async def __get_otp_user(self, email: str) -> User:
        user = await get_existing_user(email, self.user_service)
        if user.status == UserStatus.Verified:
            logger.error(f"User {email} is already verified")
            raise UserStatusException(user.status)
        return user

    async def send_otp(self, email: str) -> OTPResponse:
        await self.__get_otp_user(email)
        expire_time = await self.otp_service.send_otp(email)
        return OTPResponse(
            email=email, expire_time=expire_time, message="OTP Sent Successfully."
        )

    async def verify_otp(self, otp_verify: OTPVerifyRequest) -> OTPVerifyResponse:
        user = await self.__get_otp_user(otp_verify.email)
        if await self.otp_service.verify_otp(otp_verify.email, otp_verify.otp):
            await self.user_service.update_user_status(
                user_id=user.id, status="verified"
            )
            return OTPVerifyResponse(
                email=otp_verify.email,
                status=UserStatus.Verified,
                message="User Verified Successfully.",
            )

    async def signin(self, credentials: OAuth2PasswordRequestFormStrict) -> Token:
        if credentials.grant_type != "password":
            raise InvalidGrantTypeException(grant_type=credentials.grant_type)
        user_signin = UserSignIn(
            email=credentials.username, password=credentials.password
        )
        if await self.signin_service.signin(user_signin):
            return await self.token_manager.generate_tokens(user_signin.email)

    async def refresh_token(self, token: str) -> Token:
        payload = await self.token_manager.decode_token(
            token=token, token_type="refresh"
        )
        email = payload.sub
        return await self.token_manager.generate_tokens(email)
