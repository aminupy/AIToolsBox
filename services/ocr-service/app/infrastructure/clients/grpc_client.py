from datetime import timedelta
from typing import Annotated, Tuple
import grpc
from loguru import logger
import tenacity
from fastapi import Depends, HTTPException, status
from aiobreaker import CircuitBreaker
from tenacity import retry, stop_after_attempt, wait_fixed

from app.core.config import get_settings, Settings
from app.infrastructure.grpc import media_pb2, media_pb2_grpc

breaker = CircuitBreaker(fail_max=3, timeout_duration=timedelta(seconds=60))


class GRPCClient:
    def __init__(self, config: Annotated[Settings, Depends(get_settings)]):
        self.config = config
        self.channel = None
        self.stub = None

    async def __initialize(self) -> None:
        if self.channel is None or self.stub is None:
            options = [('grpc.max_message_length', 100 * 1024 * 1024),
                       ('grpc.max_receive_message_length', 100 * 1024 * 1024),
                       ('grpc.max_send_message_length', 100 * 1024 * 1024)]
            self.channel = grpc.aio.insecure_channel(self.config.MEDIA_SERVICE_GRPC, options=options)
            self.stub = media_pb2_grpc.MediaServiceStub(self.channel)
            logger.info(f"GRPC Client connected to {self.config.MEDIA_SERVICE_GRPC}")

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    @breaker
    async def download_media(self, media_id: str, media_type: str, user_id: str) -> bytes:
        try:
            request = media_pb2.MediaRequest(media_id=media_id, media_type=media_type)
            metadata = [('user', user_id)]
            response = await self.stub.DownloadMedia(request, metadata=metadata)
            logger.info(f"Media {media_id} downloaded")
            return response.media_data
        except grpc.aio.AioRpcError as e:
            logger.error(f"Error downloading media {media_id} - {e}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Service unavailable - {e}",
            )

    async def request_media(self, media_id: str, media_type: str, user_id: str) -> bytes:
        try:
            logger.info(f"Requesting media {media_id}")
            return await self.download_media(media_id, media_type, user_id)
        except tenacity.RetryError:
            logger.error(f"GRPC Media Service unavailable")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Service unavailable",
            )

    async def __aenter__(self):
        await self.__initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.channel.close()
