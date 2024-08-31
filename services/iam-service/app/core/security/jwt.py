from datetime import datetime, timedelta, UTC
from typing import Optional, Union, Literal

from fastapi import Depends
from jose import jwt, JWTError
from app.core.config import get_settings, Settings
from app.domain.schemas.token import TokenPayload, Token


class TokenManager:

    def __init__(self, config: Settings = Depends(get_settings)):
        self.config = config

    async def __create_token(
            self,
            subject: Union[str, int],
            token_type: Literal["access", "refresh"],
            expire_time: timedelta
    ) -> str:
        expire = datetime.now(UTC) + expire_time

        iat = datetime.now(UTC)
        to_encode = TokenPayload(sub=str(subject), type=token_type, exp=expire, iat=iat)

        encoded_jwt = jwt.encode(to_encode.model_dump(), self.config.JWT_SECRET_KEY, algorithm=self.config.JWT_ALGORITHM)
        # convert it to "utf-8" string
        return f'Bearer {encoded_jwt}'

    async def create_access_token(self, subject: Union[str, int]) -> str:
        return await self.__create_token(
            subject, "access", timedelta(minutes=self.config.ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    async def create_refresh_token(self, subject: Union[str, int]) -> str:
        return await self.__create_token(
            subject, "refresh", timedelta(days=self.config.REFRESH_TOKEN_EXPIRE_DAYS)
        )

    async def generate_tokens(self, subject: Union[str, int]) -> Token:
        access_token = await self.create_access_token(subject)
        refresh_token = await self.create_refresh_token(subject)
        return Token(
            access_token=access_token,
            access_token_expires=self.config.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            refresh_token=refresh_token,
            refresh_token_expires=self.config.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60
        )

    async def decode_token(self, token: str, token_type: Literal["access", "refresh"]) -> Optional[TokenPayload]:
        try:
            payload = jwt.decode(token, self.config.JWT_SECRET_KEY, algorithms=[self.config.JWT_ALGORITHM])
            if payload.get("type") != token_type:
                return None
            return TokenPayload(**payload)
        except JWTError:
            return None
