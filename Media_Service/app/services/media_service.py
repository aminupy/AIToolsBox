from fastapi import Depends, UploadFile, HTTPException, status

from typing import Annotated, Generator, Callable, Any

from fastapi import Depends, UploadFile, HTTPException, status

from app.domain.models.media_model import MediaGridFSModel
from app.domain.schemas.media_schema import MediaSchema
from app.infrastructure.repositories.media_repository import MediaRepository
from app.infrastructure.storage.gridfs_storage import GridFsStorage


class MediaService:
    def __init__(
        self,
        media_repository: Annotated[MediaRepository, Depends()],
        storage: Annotated[GridFsStorage, Depends()],
    ):
        self.media_repository = media_repository
        self.storage = storage

    async def create_media(self, file: UploadFile, user_id: str) -> MediaSchema:
        storage_id = await self.storage.save_file(file)
        media = MediaGridFSModel(
            storage_id=storage_id,
            filename=file.filename,
            content_type=file.content_type,
            size=file.size,
            user_id=user_id,
        )
        await self.media_repository.create_media(media)

        return MediaSchema(
            mongo_id=str(media.mongo_id),
            filename=media.filename,
            content_type=media.content_type,
            size=media.size,
            upload_date=media.upload_date,
            user_id=media.user_id,
            message="Media uploaded successfully",
        )

    async def get_media(
        self, media_id: str
    ) -> tuple[MediaSchema, Callable[[], Generator[Any, Any, None]]]:
        media = await self.media_repository.get_media(media_id)
        file = await self.storage.get_file(media.storage_id)
        if not media or not file:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Media not found"
            )

        def file_stream():
            yield file

        return (
            MediaSchema(
                mongo_id=media.mongo_id,
                filename=media.filename,
                content_type=media.content_type,
                size=media.size,
                upload_date=media.upload_date,
                user_id=media.user_id,
                message="Media downloaded successfully",
            ),
            file_stream,
        )
