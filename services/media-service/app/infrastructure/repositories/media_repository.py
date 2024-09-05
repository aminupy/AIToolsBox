from typing import Annotated
from loguru import logger
from bson import ObjectId
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.db.database import get_db
from app.domain.models.media import MediaGridFSModel


class MediaRepository:
    def __init__(self, db: Annotated[AsyncIOMotorClient, Depends(get_db)]):
        self.collection = db["media"]

    async def create_media(self, media: MediaGridFSModel) -> MediaGridFSModel:
        result = await self.collection.insert_one(media.dict())
        media.id = result.inserted_id
        logger.info(f"Media {media.name} created")
        return media

    async def get_media(self, media_id: ObjectId) -> MediaGridFSModel:
        media = await self.collection.find_one({"_id": media_id})
        return (
            MediaGridFSModel(
                id=str(media["_id"]),
                storage_id=str(media["storage_id"]),
                name=media["name"],
                type=media["content_type"],
                size=media["size"],
                upload_date=media["upload_date"],
                metadata=media["metadata"],
                user_id=media["user_id"],
            )
            if media
            else None
        )
