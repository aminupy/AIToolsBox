import bson
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends
from typing import Annotated

from app.core.config import get_settings
from app.core.db.database import get_db
from app.domain.models.media_model import MediaModel


class MediaRepository:
    def __init__(self, db: Annotated[AsyncIOMotorClient, Depends(get_db)]):
        self.collection = db['media']

    async def create_media(self, media: MediaModel) -> MediaModel:
        result = await self.collection.insert_one(media.dict())
        media.mongo_id = result.inserted_id
        return media

    async def get_media(self, media_id: str) -> MediaModel:
        media = await self.collection.find_one({'_id': ObjectId(media_id)})
        return MediaModel(
            mongo_id=str(media['_id']),
            storage_id=str(media['storage_id']),
            filename=media['filename'],
            content_type=media['content_type'],
            size=media['size'],
            upload_date=media['upload_date'],
            metadata=media['metadata'],
            user_id=media['user_id']
        ) if media else None
