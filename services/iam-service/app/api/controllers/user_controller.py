from typing import Annotated, Dict
from uuid import UUID
from fastapi import Depends

from app.domain.schemas.user import (
    UserInitialSignUp,
    UserInitialSignUpResponse,
    UserFinalSignUp,
)
from app.services import UserService, SignUpService
from app.utils.decorators import handle_exceptions


class UserController:
    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        signup_service: Annotated[SignUpService, Depends()],
    ):
        self.user_service = user_service
        self.signup_service = signup_service

    @handle_exceptions
    async def initialize_signup(
        self, user: UserInitialSignUp
    ) -> UserInitialSignUpResponse:
        return await self.signup_service.initialize_signup(user)

    @handle_exceptions
    async def finalize_signup(
        self, user_id: UUID, user: UserFinalSignUp
    ) -> Dict[str, str]:
        await self.signup_service.finalize_signup(user_id, user)
        return {"message": "User signed up successfully"}
