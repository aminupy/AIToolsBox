from datetime import timedelta
from typing import Annotated
from loguru import logger
import httpx
import tenacity
from fastapi import Depends, HTTPException, status
from app.core.config import get_settings, Settings
from tenacity import retry, stop_after_attempt, wait_fixed
from aiobreaker import CircuitBreaker

breaker = CircuitBreaker(fail_max=3, timeout_duration=timedelta(seconds=60))


class HTTPClient:
    def __init__(self, config: Settings = Depends(get_settings)):
        self.config = config
        self.http_client = httpx.AsyncClient()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    @breaker
    async def _request(
        self, method: str, url: str, headers: dict = None, data: dict = None
    ):
        async with httpx.AsyncClient(
            timeout=10
        ) as client:  # Using async with to manage lifecycle
            try:
                response = await client.request(method, url, headers=headers, json=data)
                response.raise_for_status()
                logger.info(f"HTTP request to {url} successful")
                return response
            except httpx.RequestError as e:
                logger.error(f"Error making request to {url} - {e}")
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail=f"Service unavailable - {e}",
                )
            except httpx.HTTPStatusError as e:
                logger.error(f"Error making request to {url} - {e}")
                raise HTTPException(
                    status_code=e.response.status_code,
                    detail=e.response.json(),
                )

    async def get(self, url: str, headers: dict = None):
        try:
            logger.info(f"Making GET request to {url}")
            return await self._request("GET", url, headers=headers)
        except tenacity.RetryError:
            logger.error(f"HTTP Service unavailable")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Service unavailable",
            )

    async def post(self, url: str, headers: dict = None, data: dict = None):
        try:
            logger.info(f"Making POST request to {url}")
            return await self._request("POST", url, headers=headers, data=data)
        except tenacity.RetryError:
            logger.error(f"HTTP Service unavailable")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Service unavailable",
            )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.http_client.aclose()
