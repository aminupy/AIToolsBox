from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from app.infrastructure.clients.iam_client import IAMClient
from app.domain.schemas.token_schema import TokenDataSchema
from app.core.config import get_settings


config = get_settings()


async def get_current_user(
    request: Request, client: Annotated[IAMClient, Depends()]
) -> TokenDataSchema:
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    async with client:
        return await client.validate_token(token.split("Bearer ")[1])
