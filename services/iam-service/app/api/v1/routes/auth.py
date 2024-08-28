from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.schemas.user import UserInitialSignUp, UserFinalSignUp, UserSignIn, UserInitialSignUpResponse
from app.domain.schemas.otp import OTPVerifyRequest, OTPResponse, OTPRequest, OTPVerifyResponse
from app.domain.schemas.token import Token, TokenPayload
from app.api.v1.controllers.auth_controller import AuthController

auth_router = APIRouter()
AuthControllerDep = Annotated[AuthController, Depends()]


@auth_router.post(
    "/initialize-signup",
    response_model=UserInitialSignUpResponse,
    status_code=status.HTTP_201_CREATED
)
async def initialize_signup(
        user: UserInitialSignUp, auth_controller: AuthControllerDep
) -> OTPResponse:
    return await auth_controller.initialize_signup(user)


@auth_router.post(
    "/finalize-signup",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
async def finalize_signup(
        user: UserFinalSignUp, auth_controller: AuthControllerDep
) -> Token:
    return await auth_controller.finalize_signup(user)


@auth_router.post(
    "/signin",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
async def signin(
        user: UserSignIn, auth_controller: AuthControllerDep
) -> Token:
    return await auth_controller.signin(user)


@auth_router.post(
    "/request-otp",
    response_model=OTPResponse,
    status_code=status.HTTP_201_CREATED,
)
async def request_otp(
    otp_request: OTPRequest, auth_controller: AuthControllerDep
) -> OTPResponse:
    return await auth_controller.send_otp(otp_request.email)


@auth_router.post(
    "/verify-otp",
    response_model=OTPVerifyResponse,
    status_code=status.HTTP_200_OK,
)
async def verify_otp(
    otp_verify: OTPVerifyRequest,
    auth_controller: AuthControllerDep
) -> OTPVerifyResponse:
    return await auth_controller.verify_otp(otp_verify)
