from typing import Annotated
from loguru import logger
from fastapi import Depends
from app.core.config import get_settings, Settings
from app.domain.schemas.token_user import TokenUser
from app.infrastructure.clients.http_client import HTTPClient


class IAMClient:
    def __init__(
        self,
        http_client: Annotated[HTTPClient, Depends()],
        config: Settings = Depends(get_settings),
    ):
        self.config = config
        self.http_client = http_client

    async def get_user(self, token: str) -> TokenUser:
        headers = {"Authorization": f"Bearer {token}"}
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.IAM_URL}/users/me", headers=headers
            )
            response.raise_for_status()
            logger.info(f"Token {token} validated")
            user = response.json()
            return TokenUser(
                id=user.id,
                fullname=user.fullname,
                email=user.email
            )
