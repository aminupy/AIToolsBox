from datetime import timedelta
from typing import Annotated
import grpc
from fastapi import Depends
from aiobreaker import CircuitBreaker
from tenacity import retry, stop_after_attempt, wait_fixed

from app.core.config import get_settings, Settings
from app.infrastructure.clients.grpc_client import GRPCClient


class MediaClient:
    def __init__(self, grpc_client: Annotated[GRPCClient, Depends()]):
        self.grpc_client = grpc_client

    async def request_media(self, media_id: str, media_type: str, user_id: str) -> bytes:
        async with self.grpc_client as client:
            return await client.request_media(media_id, media_type, user_id)


