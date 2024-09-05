from typing import Annotated, Dict
from fastapi.security import OAuth2PasswordRequestFormStrict
from fastapi import Depends, Response

from app.domain.schemas.otp import OTPResponse, OTPVerifyRequest, OTPVerifyResponse
from app.domain.schemas.token import Token
from app.utils import handle_exceptions
from app.services import AuthService


class AuthController:
    def __init__(self, auth_service: Annotated[AuthService, Depends()]):
        self.auth_service = auth_service

    @handle_exceptions
    async def __set_cookies(self, response: Response, tokens: Token):
        response.set_cookie(
            key="access_token",
            value=tokens.access_token,
            httponly=True,
            secure=True,
            samesite="strict",
            max_age=tokens.access_token_expires,
        )

        # Set the refresh token as an HTTP-only, Secure cookie
        response.set_cookie(
            key="refresh_token",
            value=tokens.refresh_token,
            httponly=True,
            secure=True,
            samesite="strict",
            max_age=tokens.refresh_token_expires,
        )

    @handle_exceptions
    async def signin(
        self, credentials: OAuth2PasswordRequestFormStrict, response: Response
    ) -> Dict[str, str]:
        tokens = await self.auth_service.signin(credentials)
        await self.__set_cookies(response, tokens)

        return {
            "message": "User signed in successfully",
        }

    @handle_exceptions
    async def refresh_token(
        self, refresh_token: str, response: Response
    ) -> Dict[str, str]:
        tokens = await self.auth_service.refresh_token(refresh_token)
        await self.__set_cookies(response, tokens)

        return {"message": "Token refreshed successfully"}

    @handle_exceptions
    async def send_otp(self, email: str) -> OTPResponse:
        return await self.auth_service.send_otp(email)

    @handle_exceptions
    async def verify_otp(self, otp_verify: OTPVerifyRequest) -> OTPVerifyResponse:
        return await self.auth_service.verify_otp(otp_verify)
