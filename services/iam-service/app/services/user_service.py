from typing import Annotated, Dict
from uuid import UUID
from loguru import logger
from fastapi import Depends

from app.domain.models.user import User
from app.domain.schemas.user_schema import UserCreateSchema
from app.infrastructure.repositories.user_repository import UserRepository
from app.services.auth_services.hash_sevice import HashService
from app.services.base_service import BaseService


class UserService(BaseService):
    def __init__(
        self,
        user_repository: Annotated[UserRepository, Depends()],
        hash_service: Annotated[HashService, Depends()],
    ) -> None:
        super().__init__()
        self.user_repository = user_repository
        self.hash_service = hash_service

    async def create_user(self, user_body: UserCreateSchema) -> User:
        logger.info(f"Creating user with mobile number {user_body.mobile_number}")
        return self.user_repository.create_user(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                mobile_number=user_body.mobile_number,
                hashed_password=self.hash_service.hash_password(user_body.password),
            )
        )

    async def update_user(self, user_id: int, update_fields: Dict) -> User:
        logger.info(f"Updating user with id {user_id}")
        return self.user_repository.update_user(user_id, update_fields)

    async def delete_user(self, user: User) -> None:
        logger.info(f"Deleting user with id {user.id}")
        return self.user_repository.delete_user(user)

    async def get_user(self, user_id: UUID) -> User:
        logger.info(f"Fetching user with id {user_id}")
        return self.user_repository.get_user(user_id)

    async def get_user_by_mobile_number(self, mobile_number: str) -> User:
        logger.info(f"Fetching user with mobile number {mobile_number}")
        return self.user_repository.get_user_by_mobile_number(mobile_number)
