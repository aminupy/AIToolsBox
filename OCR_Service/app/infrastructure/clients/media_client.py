from typing import Annotated
import grpc
from fastapi import Depends
from app.core.config import get_settings, Settings
from app.infrastructure.grpc import media_pb2, media_pb2_grpc


class MediaClient:
    def __init__(self, config: Annotated[Settings, Depends(get_settings)]):
        self.config = config
        self.channel = None
        self.stub = None

    async def download_media(self, media_id: str, media_type: str, user_id: str) -> bytes:
        if self.channel is None or self.stub is None:
            options = [('grpc.max_message_length', 100 * 1024 * 1024),
                       ('grpc.max_receive_message_length', 100 * 1024 * 1024),
                       ('grpc.max_send_message_length', 100 * 1024 * 1024)]
            self.channel = grpc.aio.insecure_channel(self.config.MEDIA_SERVICE_GRPC, options=options)
            self.stub = media_pb2_grpc.MediaServiceStub(self.channel)

        request = media_pb2.MediaRequest(media_id=media_id, media_type=media_type)
        metadata = [('user', user_id)]
        response = await self.stub.DownloadMedia(request, metadata=metadata)
        return response.media_data


