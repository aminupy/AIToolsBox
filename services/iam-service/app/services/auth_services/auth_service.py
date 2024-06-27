from datetime import datetime, timedelta, timezone
from typing import Annotated
from loguru import logger
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.domain.models.user import User
from app.domain.schemas.token_schema import TokenSchema
from app.domain.schemas.user_schema import UserLoginSchema
from app.services.auth_services.hash_sevice import HashService
from app.services.base_service import BaseService
from app.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/Token")


class AuthService(BaseService):
    def __init__(
        self,
        hash_service: Annotated[HashService, Depends()],
        user_service: Annotated[UserService, Depends()],
    ) -> None:
        super().__init__()
        self.user_service = user_service
        self.hash_service = hash_service

    async def authenticate_user(self, user: UserLoginSchema) -> TokenSchema:
        existing_user = await self.user_service.get_user_by_mobile_number(
            user.mobile_number
        )
        logger.info(f"Authenticating user with mobile number {user.mobile_number}")

        if not existing_user:
            logger.error(f"User with mobile number {user.mobile_number} does not exist")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist"
            )

        if not existing_user.is_verified:
            logger.error(f"User with mobile number {user.mobile_number} is not verified")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User is not verified"
            )

        if not self.hash_service.verify_password(
            user.password, existing_user.hashed_password
        ):
            logger.error(f"Invalid password for user with mobile number {user.mobile_number}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = self.create_access_token(data={"sub": str(existing_user.id)})

        logger.info(f"User with mobile number {user.mobile_number} authenticated successfully")
        return TokenSchema(access_token=access_token, token_type="bearer")

    def create_access_token(self, data: dict) -> str:
        logger.info("Creating access token")
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            self.config.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, self.config.JWT_SECRET_KEY, algorithm=self.config.JWT_ALGORITHM
        )
        return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_service: Annotated[UserService, Depends()],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    logger.info(f"Validating token {token}")
    try:
        payload = jwt.decode(
            token,
            user_service.config.JWT_SECRET_KEY,
            algorithms=[user_service.config.JWT_ALGORITHM],
        )
        user_id: str = payload.get("sub")
        user = await user_service.get_user(user_id)
        if user_id is None:
            logger.error("Could not validate credentials")
            raise credentials_exception
    except jwt.PyJWTError:
        logger.error("Error decoding token")
        raise credentials_exception

    logger.info(f"User with id {user_id} validated successfully")
    return user
