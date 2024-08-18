from fastapi import Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from loguru import logger

from app.domain.models.user import User
from app.domain.schemas.user import (
    UserInitialSignUp,
    UserResponse
)
from app.services.auth_service import AuthService, get_current_user
from app.services.signup_service import RegisterService

user_router = APIRouter()


@user_router.post(
    "/signup",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
async def signup(
    user: UserInitialSignUp, signup_service: Annotated[RegisterService, Depends()]
) -> UserCreateResponseSchema:
    logger.info(f"Registering user with mobile number {user.mobile_number}")
    return await register_service.register_user(user)


@user_router.post("/Token", response_model=TokenSchema, status_code=status.HTTP_200_OK)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
) -> TokenSchema:

    logger.info(f"Logging in user with mobile number {form_data.username}")
    return await auth_service.authenticate_user(
        UserLoginSchema(mobile_number=form_data.username, password=form_data.password)
    )


@user_router.post(
    "/VerifyOTP", response_model=VerifyOTPResponseSchema, status_code=status.HTTP_200_OK
)
async def verify_otp(
    verify_user_schema: VerifyOTPSchema,
    register_service: Annotated[RegisterService, Depends()],
) -> VerifyOTPResponseSchema:
    logger.info(f"Verifying OTP for user with mobile number {verify_user_schema.mobile_number}")
    return await register_service.verify_user(verify_user_schema)


@user_router.post(
    "/ResendOTP",
    response_model=ResendOTPResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def resend_otp(
    resend_otp_schema: ResendOTPSchema,
    register_service: Annotated[RegisterService, Depends()],
) -> ResendOTPResponseSchema:
    logger.info(f"Resending OTP for user with mobile number {resend_otp_schema.mobile_number}")
    return await register_service.resend_otp(resend_otp_schema)


@user_router.get("/Me", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def read_users_me(current_user: User = Depends(get_current_user)) -> UserSchema:
    logger.info(f"Getting user with mobile number {current_user.email}")
    return current_user
