from typing import Annotated
from loguru import logger
from fastapi import Depends

from app.core.security import Hasher, hash_provider, create_access_token, create_refresh_token
from app.core.exceptions import InvalidPasswordException, UserNotFoundException, UserStatusException
from app.domain.models.user import User
from app.domain.schemas.user import UserSignIn
from app.domain.schemas.token import Token
from app.services.user_service import UserService
from app.domain.models.user_status import UserStatus
from app.services.base_service import BaseService


class SignInService(BaseService):
    def __init__(
        self,
        hash_service: Annotated[Hasher, Depends(hash_provider)],
        user_service: Annotated[UserService, Depends()]
    ) -> None:
        super().__init__()
        self.user_service = user_service
        self.hash_service = hash_service

    async def signin(self, user_signin: UserSignIn) -> Token:
        db_user = await self.user_service.get_user_by_email(user_signin.email)
        await self._validate_user(db_user, user_signin)

        return await self._generate_tokens(user_signin.email)

    async def _validate_user(self, db_user: User, user_signin: UserSignIn) -> None:
        """
        Validates the user's existence, status, and password.
        Raises an exception if any validation fails.
        """
        if not db_user:
            logger.error(f"User with email {user_signin.email} not found")
            raise UserNotFoundException(user_signin.email)

        if db_user.status != UserStatus.ACTIVE:
            logger.error(f"User with email {db_user.email} is not active")
            raise UserStatusException("User is not active")

        is_valid = await self.hash_service.verify_password(user_signin.password, db_user.hashed_password)
        if is_valid is False:
            logger.error(f"Invalid password for email {db_user.email}")
            raise InvalidPasswordException(email=db_user.email)

    @staticmethod
    async def _generate_tokens(email: str) -> Token:
        access_token = create_access_token(email)
        refresh_token = create_refresh_token(email)
        return Token(access_token=access_token, refresh_token=refresh_token)
