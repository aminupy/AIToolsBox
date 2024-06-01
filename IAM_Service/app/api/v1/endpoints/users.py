from typing import Annotated
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.models.user import User
from app.services.user_service import UserService
from app.services.auth_services.auth_service import AuthService, get_current_user
from app.services.register_service import RegisterService

from app.domain.schemas.user_schema import (
    UserCreateSchema,
    UserCreateResponseSchema,
    UserSchema,
    UserLoginSchema,
    VerifyOTPSchema,
    VerifyOTPResponseSchema,
    ResendOTPSchema,
    ResendOTPResponseSchema,
)
from app.domain.schemas.token_schema import TokenSchema, TokenDataSchema

user_router = APIRouter()


@user_router.post(
    "/Register",
    response_model=UserCreateResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    user: UserCreateSchema, register_service: Annotated[RegisterService, Depends()]
) -> UserCreateResponseSchema:
    return await register_service.register_user(user)


@user_router.post("/Token", response_model=TokenSchema, status_code=status.HTTP_200_OK)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends()],
) -> TokenSchema:

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
    return await register_service.resend_otp(resend_otp_schema)


@user_router.get("/Me", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def read_users_me(current_user: User = Depends(get_current_user)) -> UserSchema:
    return current_user
