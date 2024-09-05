from uuid import UUID

from fastapi import Depends
from typing import Annotated
from loguru import logger

from app.core.exceptions import UserNotFoundException, UserAlreadyExistsException
from app.domain.models.user import User
from app.services.user_service import UserService


async def __get_user(
    email: str, user_service: Annotated[UserService, Depends()]
) -> User:
    existing_user = await user_service.get_user_by_email(email)
    if not existing_user:
        logger.error(f"No account with email {email} found")
        raise UserNotFoundException(email)
    return existing_user


async def get_existing_user_by_id(
    user_id: UUID, user_service: Annotated[UserService, Depends()]
) -> User:
    existing_user = await user_service.get_user(user_id)
    if not existing_user:
        logger.error(f"No account with id {user_id} found")
        raise UserNotFoundException(str(user_id))
    return existing_user


async def get_existing_user(
    email: str, user_service: Annotated[UserService, Depends()]
) -> User:
    return await __get_user(email, user_service)


async def ensure_user_exists(
    email: str, user_service: Annotated[UserService, Depends()]
) -> None:
    await __get_user(email, user_service)


async def ensure_user_does_not_exist(
    email: str, user_service: Annotated[UserService, Depends()]
) -> None:
    existing_user = await user_service.get_user_by_email(email)
    if existing_user:
        logger.error(f"Account with email {email} already exists")
        raise UserAlreadyExistsException(email)
