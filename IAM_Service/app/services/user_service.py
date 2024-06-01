from fastapi import Depends
from typing import Annotated, Dict
from uuid import UUID

from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.schemas.user_schema import UserCreateSchema
from app.domain.models.user import User
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
        return self.user_repository.create_user(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                email=user_body.email,
                mobile_number=user_body.mobile_number,
                hashed_password=self.hash_service.hash_password(user_body.password),
            )
        )

    async def update_user(self, user_id: int, update_fields: Dict) -> User:
        return self.user_repository.update_user(user_id, update_fields)

    async def delete_user(self, user: User) -> None:
        return self.user_repository.delete_user(user)

    async def get_user(self, user_id: UUID) -> User:
        return self.user_repository.get_user(user_id)

    async def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)

    async def get_user_by_mobile_number(self, mobile_number: str) -> User:
        return self.user_repository.get_user_by_mobile_number(mobile_number)
