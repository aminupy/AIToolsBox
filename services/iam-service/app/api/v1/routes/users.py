from fastapi import Depends, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from loguru import logger

from app.domain.schemas.user import (
    UserResponse
)
from app.api.v1.dependencies import get_current_user

user_router = APIRouter()


@user_router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK
)
async def read_users_me(current_user: UserResponse = Depends(get_current_user)) -> UserResponse:
    logger.info(f"Getting user with email {current_user.email}")
    return current_user
