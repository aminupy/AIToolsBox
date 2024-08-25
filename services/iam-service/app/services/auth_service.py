from datetime import datetime, timedelta, timezone
from typing import Annotated
from loguru import logger
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.domain.schemas.otp import OTPResponse, OTPVerify
from app.domain.schemas.token import Token
from app.domain.schemas.user import UserSignIn, UserInitialSignUp, UserFinalSignUp
from app.core.security import hash_provider, Hasher
from app.services.base_service import BaseService
from app.services.sub_services import SignUpService, SignInService


class AuthService(BaseService):
    def __init__(
        self,
        signup_service: Annotated[SignUpService, Depends()],
        signin_service: Annotated[SignInService, Depends()]
    ) -> None:
        super().__init__()
        self.signup_service = signup_service
        self.signin_service = signin_service

    async def initialize_signup(self, user: UserInitialSignUp) -> OTPResponse:
        return await self.signup_service.initialize_signup(user)

    async def verify_signup(self, otp_verify: OTPVerify) -> dict:
        return await self.signup_service.verify_signup(otp_verify)

    async def finalize_signup(self, user: UserFinalSignUp) -> Token:
        if await self.signup_service.finalize_signup(user):
            return await self.signin_service.signin(UserSignIn(email=user.email, password=user.password))

    async def signin(self, user: UserSignIn) -> Token:
        return await self.signin_service.signin(user)





