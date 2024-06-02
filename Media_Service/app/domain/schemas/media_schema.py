from datetime import datetime
from uuid import UUID

from bson import ObjectId
from pydantic import BaseModel
from typing import Optional
from app.domain.models.media_model import MediaModel, MediaBaseModel


class MediaCreateResponseSchema(BaseModel):
    media: MediaModel
    message: str

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}


class MediaGetSchema(BaseModel):
    mongo_id: str


class MediaGetResponseSchema(BaseModel):
    media: MediaModel
    message: str

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True
