from datetime import datetime, timedelta, timezone, UTC
from typing import Optional, Union, Literal
from jose import jwt, JWTError
from app.core.config import get_settings
from app.domain.schemas.token import TokenPayload

config = get_settings()


def __create_token(
        subject: Union[str, int],
        expire_time: timedelta
) -> str:
    expire = datetime.now(UTC) + expire_time

    iat = datetime.now(UTC)
    to_encode = TokenPayload(sub=str(subject), exp=expire, iat=iat)

    encoded_jwt = jwt.encode(to_encode.model_dump(), config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt


def create_access_token(subject: Union[str, int]) -> str:
    return __create_token(subject, timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES))


def create_refresh_token(subject: Union[str, int]) -> str:
    return __create_token(subject, timedelta(days=config.REFRESH_TOKEN_EXPIRE_DAYS))


def decode_token(token: str) -> Optional[TokenPayload]:
    try:
        payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        return TokenPayload(**payload)
    except JWTError:
        return None
