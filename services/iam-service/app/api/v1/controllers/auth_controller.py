from typing import Annotated
from loguru import logger
from fastapi import Depends, HTTPException, status
from app.core.exceptions import (
    UserAlreadyExistsException,
    OTPServiceException,
    UserNotFoundException,
    UserStatusException, InvalidPasswordException
)
from app.domain.schemas.otp import OTPResponse, OTPVerifyRequest, OTPVerifyResponse
from app.domain.schemas.token import Token
from app.domain.schemas.user import UserInitialSignUp, UserFinalSignUp, UserSignIn, UserInitialSignUpResponse
from app.utilites import handle_exceptions
from app.services import AuthService


class AuthController:
    def __init__(self, auth_service: Annotated[AuthService, Depends()]):
        self.auth_service = auth_service

    @handle_exceptions
    async def initialize_signup(self, user: UserInitialSignUp) -> UserInitialSignUpResponse:
        return await self.auth_service.initialize_signup(user)

    @handle_exceptions
    async def finalize_signup(self, user: UserFinalSignUp) -> Token:
        return await self.auth_service.finalize_signup(user)

    @handle_exceptions
    async def signin(self, user: UserSignIn) -> Token:
        return await self.auth_service.signin(user)

    @handle_exceptions
    async def send_otp(self, email: str) -> OTPResponse:
        return await self.auth_service.send_otp(email)

    @handle_exceptions
    async def verify_otp(self, otp_verify: OTPVerifyRequest) -> OTPVerifyResponse:
        return await self.auth_service.verify_otp(otp_verify)
