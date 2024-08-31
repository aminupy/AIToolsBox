from typing import Annotated, Dict, Literal
from uuid import UUID
from loguru import logger
from fastapi import Depends

from app.domain.models.user import User
from app.domain.models.user_status import UserStatus
from app.domain.schemas.user import UserFinalSignUp, UserInitialSignUp
from app.infrastructure.repositories.user_repository import UserRepository
from app.core.security import Hasher


class UserService:
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        hasher: Annotated[Hasher, Depends()],
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.hasher = hasher

    async def initialize_user(self, initial_user: UserInitialSignUp):
        logger.info(f"Initializing user with email {initial_user.email}")
        return self.user_repository.create_user(
            User(email=initial_user.email, status=UserStatus.UnVerified)
        )

    async def finalize_user(self, user_id: str, final_user: UserFinalSignUp) -> User:
        logger.info(f"Finalizing user with email {final_user.email}")
        finalized_user = {
            "fullname": final_user.fullname,
            "hashed_password": await self.hasher.hash_password(final_user.password),
            "status": UserStatus.ACTIVE,
        }
        return self.user_repository.update_user(user_id, updated_user=finalized_user)

    async def update_user_status(
        self,
        user_id: str,
        status: Literal["unverified", "verified", "active", "inactive"],
    ) -> User:
        logger.info(f"Updating user {user_id} status to {status}")
        return self.user_repository.update_user(
            user_id=user_id, updated_user={"status": UserStatus(status)}
        )

    async def update_user(self, user_id: str, update_fields: Dict) -> User:
        logger.info(f"Updating user with id {user_id}")
        return self.user_repository.update_user(user_id, update_fields)

    async def delete_user(self, user: User) -> None:
        logger.info(f"Deleting user with id {user.id}")
        return self.user_repository.delete_user(user)

    async def get_user(self, user_id: UUID) -> User:
        logger.info(f"Fetching user with id {user_id}")
        return self.user_repository.get_user(user_id)

    async def get_user_by_email(self, email: str) -> User:
        logger.info(f"Fetching user with email {email}")
        return self.user_repository.get_user_by_email(email)
