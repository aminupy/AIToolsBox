from fastapi import Depends
from typing import Annotated

from app.infrastructure.repositories.user_repository import UserRepository
from app.domain.schemas.user_schemas import UserCreateSchema
from app.domain.models.user import User


class UserService:
    def __init__(self, user_repository: Annotated[UserRepository, Depends()]) -> None:
        self.user_repository = user_repository

    def create_user(self, user_body: UserCreateSchema) -> User:
        return self.user_repository.create_user(
            User(
                first_name=user_body.first_name,
                last_name=user_body.last_name,
                email=user_body.email,
                mobile_number=user_body.mobile_number,
                hashed_password=user_body.password
            )
        )