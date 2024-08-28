from app.core.exceptions import (
    UserStatusException
)
from app.core.security import Hasher
from app.domain.models.user_status import UserStatus
from app.domain.schemas.user import (
    UserInitialSignUp,
    UserFinalSignUp,
    UserInitialSignUpResponse
)
from app.services import OTPService
from app.services.base_service import BaseService
from app.services.user_service import UserService
from app.utilites.user_utils import get_existing_user, ensure_user_exists, ensure_user_does_not_exist
from typing import Annotated
from fastapi import Depends
from loguru import logger


class SignUpService(BaseService):
    def __init__(
        self,
        hash_service: Annotated[Hasher, Depends()],
        user_service: Annotated[UserService, Depends()],
        otp_service: Annotated[OTPService, Depends()],
    ) -> None:
        super().__init__()
        self.user_service = user_service
        self.hash_service = hash_service
        self.otp_service = otp_service

    async def initialize_signup(self, user: UserInitialSignUp) -> UserInitialSignUpResponse:
        await ensure_user_does_not_exist(user.email, self.user_service)

        new_user = await self.user_service.initialize_user(user)
        logger.info(f"User with email {user.email} created successfully")

        return UserInitialSignUpResponse(
            email=new_user.email,
            status=new_user.status,
            created_at=new_user.created_at,
            message="User created successfully"
        )

    async def finalize_signup(self, signup_user: UserFinalSignUp):
        user = await get_existing_user(signup_user.email, self.user_service)

        if user.status != UserStatus.Verified:
            logger.error(f"User {user.email} is not verified")
            raise UserStatusException(user.status)

        await self.user_service.finalize_user(user_id=user.id, final_user=signup_user)
        logger.info(f"User with email {user.email} signed up successfully")
