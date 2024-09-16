from fastapi import Depends, HTTPException, status
from typing import Annotated
from loguru import logger

from app.utils.fastapi_utils import OAuth2PasswordBearerWithCookie
from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.token_user import TokenUser
from app.core.config import get_settings


config = get_settings()

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl=f"http://iam.localhost/auth/token/", token_name="access_token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    client: Annotated[IAMClient, Depends()],
) -> TokenUser:

    if not token:
        logger.error("No token provided")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    logger.info(f"Validating token {token}")
    return await client.get_user(token)
