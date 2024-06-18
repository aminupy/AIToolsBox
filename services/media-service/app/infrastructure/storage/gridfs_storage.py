import asyncio
from typing import Annotated

from bson import ObjectId
from fastapi import Depends, UploadFile
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorGridFSBucket,
    AsyncIOMotorGridOut,
)

from app.core.db.database import get_db, db


class GridFsStorage:
    def __init__(self, db: Annotated[AsyncIOMotorClient, Depends(get_db)]):
        self.db = db
        self.fs = None

    async def init_fs(self):
        if not self.fs:
            self.fs = AsyncIOMotorGridFSBucket(self.db, bucket_name="media")

    async def save_file(self, file: UploadFile) -> ObjectId:
        await self.init_fs()
        grid_in = self.fs.open_upload_stream(
            file.filename, metadata={"content_type": file.content_type}
        )
        await grid_in.write(await file.read())
        await grid_in.close()
        return grid_in._id

    async def get_file(self, file_id: ObjectId) -> AsyncIOMotorGridOut:
        await self.init_fs()
        file_obj = await self.fs.open_download_stream(file_id)
        return await file_obj.read()
