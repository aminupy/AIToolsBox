from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from app.domain.schemas.user import UserInitialSignUp, UserFinalSignUp, UserSignIn
from app.domain.schemas.otp import OTPVerify, OTPResponse
from app.domain.schemas.token import Token, TokenPayload
from app.api.v1.controllers.auth_controller import AuthController

auth_router = APIRouter()
# AuthControllerDep: Annotated[AuthController, Depends()]


@auth_router.post(
    "/initialize-signup",
    response_model=OTPResponse,
    status_code=status.HTTP_201_CREATED
)
async def initialize_signup(
        user: UserInitialSignUp, auth_controller: Annotated[AuthController, Depends()]
) -> OTPResponse:
    return await auth_controller.initialize_signup(user)


@auth_router.post(
    "/verify-signup",
    status_code=status.HTTP_200_OK
)
async def verify_signup(
        otp_verify: OTPVerify, auth_controller: Annotated[AuthController, Depends()]
) -> dict:
    return await auth_controller.verify_signup(otp_verify)


@auth_router.post(
    "/finalize-signup",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
async def finalize_signup(
        user: UserFinalSignUp, auth_controller: Annotated[AuthController, Depends()]
) -> Token:
    return await auth_controller.finalize_signup(user)


@auth_router.post(
    "/signin",
    response_model=Token,
    status_code=status.HTTP_200_OK
)
async def signin(
        user: UserSignIn, auth_controller: Annotated[AuthController, Depends()]
) -> Token:
    return await auth_controller.signin(user)


