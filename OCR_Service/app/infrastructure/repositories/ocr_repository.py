from typing import Annotated

from bson import ObjectId
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.db.database import get_db
from app.domain.models.ocr_model import OCRModel


class OCRRepository:
    def __init__(self, db: Annotated[AsyncIOMotorClient, Depends(get_db)]):
        self.collection = db["ocr"]

    async def create_ocr(self, ocr: OCRModel) -> OCRModel:
        result = await self.collection.insert_one(ocr.dict())
        ocr.ocr_id = result.inserted_id
        return ocr

    async def get_media(self, ocr_id: ObjectId) -> OCRModel:
        ocr = await self.collection.find_one({"_id": ocr_id})
        ocr['ocr_id'] = ocr['_id']
        return (
            OCRModel(**ocr)
            if ocr
            else None
        )
