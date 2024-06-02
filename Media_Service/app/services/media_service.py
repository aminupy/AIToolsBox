from datetime import datetime
from uuid import UUID

from fastapi import Depends, UploadFile, File, HTTPException, status

from typing import Annotated, Generator, Tuple, Callable, Any

from motor.motor_asyncio import AsyncIOMotorGridOut

from app.infrastructure.repositories.media_repository import MediaRepository
from app.infrastructure.storage.gridfs_storage import GridFsStorage
from app.domain.models.media_model import MediaModel


class MediaService:
    def __init__(self,
                 media_repository: Annotated[MediaRepository, Depends()],
                 storage: Annotated[GridFsStorage, Depends()]
                 ):
        self.media_repository = media_repository
        self.storage = storage

    async def create_media(self, file: UploadFile, user_id: str) -> MediaModel:
        storage_id = await self.storage.save_file(file)
        media = MediaModel(
            storage_id=storage_id,
            filename=file.filename,
            content_type=file.content_type,
            size=file.size,
            user_id=user_id
        )
        return await self.media_repository.create_media(media)

    async def get_media(self, media_id: str) -> tuple[MediaModel, Callable[[], Generator[Any, Any, None]]]:
        media = await self.media_repository.get_media(media_id)
        file = await self.storage.get_file(media.storage_id)
        if not media or not file:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media not found")

        stream_file = await file.read()

        def iter_file():
            yield stream_file

        return media, iter_file

