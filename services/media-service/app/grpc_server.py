from concurrent import futures
from loguru import logger
import grpc
from app.core.config import get_settings
from app.grpc_service import media_pb2_grpc, media_pb2
from app.infrastructure.clients.iam_client import IAMClient
from app.services.media_service import MediaService
from app.infrastructure.repositories.media_repository import MediaRepository
from app.infrastructure.storage.gridfs_storage import GridFsStorage
from app.core.db.database import db


config = get_settings()


class MediaServiceServicer(media_pb2_grpc.MediaServiceServicer):
    def __init__(self, media_service: MediaService, iam_client: IAMClient):
        self.media_service = media_service
        self.iam_client = iam_client

    async def DownloadMedia(self, request, context):
        # Extract the user filed from the metadata
        user_id = dict(context.invocation_metadata()).get("user")

        try:
            media_data = await self.media_service.get_media_data(request.media_id, user_id)
            if media_data is None:
                logger.error(f"Media not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Media not found")
                return media_pb2.MediaResponse()

            logger.info(f"Media {request.media_id} retrieved")
            return media_pb2.MediaResponse(
                media_data=media_data, media_type=request.media_type
            )
        except Exception as e:
            logger.error(f"Error retrieving media: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return media_pb2.MediaResponse()


async def serve():
    options = [('grpc.max_message_length', 100 * 1024 * 1024),
               ('grpc.max_receive_message_length', 100 * 1024 * 1024),
               ('grpc.max_send_message_length', 100 * 1024 * 1024)]
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10), options=options)
    media_pb2_grpc.add_MediaServiceServicer_to_server(
        MediaServiceServicer(MediaService(
            MediaRepository(db), GridFsStorage(db)
        ), IAMClient(config)),
        server,
    )
    server.add_insecure_port(f"[::]:{config.GRPC_PORT}")
    logger.info(f"Starting Media Service gRPC server on port {config.GRPC_PORT}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    import asyncio

    asyncio.run(serve())
