from typing import Annotated

import httpx
from fastapi import Depends, HTTPException, status, Request
from app.core.config import get_settings, Settings
from app.domain.schemas.token_schema import TokenDataSchema


class IAMClient:
    def __init__(self, config: Settings = Depends(get_settings)):
        self.config = config
        self.http_client = httpx.AsyncClient()

    async def validate_token(self, token: str) -> TokenDataSchema:
        headers = {"Authorization": f"Bearer {token}"}

        try:
            response = await self.http_client.get(
                f"{self.config.IAM_URL}/api/v1/users/Me",
                headers=headers,
            )
            response.raise_for_status()
            return TokenDataSchema(**response.json())
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.json(),
            )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.http_client.aclose()
