from typing import Annotated
from fastapi import Depends
from app.core.config import get_settings, Settings
from app.domain.schemas.token_schema import TokenDataSchema
from app.infrastructure.clients.http_client import HTTPClient


class IAMClient:
    def __init__(
        self,
        http_client: Annotated[HTTPClient, Depends()],
        config: Settings = Depends(get_settings),
    ):
        self.config = config
        self.http_client = http_client

    async def validate_token(self, token: str) -> TokenDataSchema:
        headers = {"Authorization": f"Bearer {token}"}
        async with self.http_client as client:
            response = await client.get(
                f"{self.config.IAM_URL}/api/v1/users/Me", headers=headers
            )
            response.raise_for_status()
            return TokenDataSchema(**response.json())
