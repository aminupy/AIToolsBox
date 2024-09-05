from typing import Annotated, Dict
from uuid import UUID
from fastapi import APIRouter, Depends, status

from app.api.controllers.user_controller import UserController
from app.api.dependencies import get_current_user
from app.domain.schemas.user import (
    UserResponse,
    UserInitialSignUpResponse,
    UserInitialSignUp,
    UserFinalSignUp,
)

users_router = APIRouter()
UserControllerDep = Annotated[UserController, Depends()]


@users_router.post(
    "/register/",
    response_model=UserInitialSignUpResponse,
    status_code=status.HTTP_201_CREATED,
)
async def initialize_register(
    user: UserInitialSignUp, user_controller: UserControllerDep
) -> UserInitialSignUpResponse:
    return await user_controller.initialize_signup(user)


@users_router.put(
    "/register/{user_id}/",
    response_model=Dict[str, str],
    status_code=status.HTTP_200_OK,
)
async def finalize_register(
    user_id: UUID, user: UserFinalSignUp, user_controller: UserControllerDep
) -> Dict[str, str]:
    return await user_controller.finalize_signup(user_id, user)


@users_router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def me(
    current_user: Annotated[UserResponse, Depends(get_current_user)]
) -> UserResponse:
    return current_user
