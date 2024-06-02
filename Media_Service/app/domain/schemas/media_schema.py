from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel

from app.domain.models.media_model import MediaModel


class MediaSchema(MediaModel):
    message: str

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True


class MediaGetSchema(BaseModel):
    mongo_id: str
