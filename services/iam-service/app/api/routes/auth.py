from typing import Annotated, Dict
from fastapi import APIRouter, Depends, status, Response
from fastapi.security import OAuth2PasswordRequestFormStrict

from app.domain.schemas.otp import (
    OTPVerifyRequest,
    OTPResponse,
    OTPRequest,
    OTPVerifyResponse,
)
from app.api.v1.controllers.auth_controller import AuthController
from app.utilites.fastapi_utils import OAuth2PasswordBearerWithCookie

auth_router = APIRouter()
AuthControllerDep = Annotated[AuthController, Depends()]


@auth_router.post(
    "/login", response_model=Dict[str, str], status_code=status.HTTP_200_OK
)
async def login(
    credentials: Annotated[OAuth2PasswordRequestFormStrict, Depends()],
    auth_controller: AuthControllerDep,
    response: Response,
) -> Dict[str, str]:
    return await auth_controller.signin(credentials, response)


@auth_router.post(
    "/token/refresh", response_model=Dict[str, str], status_code=status.HTTP_200_OK
)
async def refresh_token(
    auth_controller: AuthControllerDep,
    token: Annotated[
        OAuth2PasswordBearerWithCookie(
            tokenUrl="/auth/token/refresh", token_name="refresh_token"
        ),
        Depends(),
    ],
    response: Response,
) -> Dict[str, str]:
    return await auth_controller.refresh_token(token, response=response)


@auth_router.post(
    "/otp/request",
    response_model=OTPResponse,
    status_code=status.HTTP_201_CREATED,
)
async def request_otp(
    otp_request: OTPRequest, auth_controller: AuthControllerDep
) -> OTPResponse:
    return await auth_controller.send_otp(otp_request.email)


@auth_router.post(
    "/otp/verify",
    response_model=OTPVerifyResponse,
    status_code=status.HTTP_200_OK,
)
async def verify_otp(
    otp_verify: OTPVerifyRequest, auth_controller: AuthControllerDep
) -> OTPVerifyResponse:
    return await auth_controller.verify_otp(otp_verify)
