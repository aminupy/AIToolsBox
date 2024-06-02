from typing import Annotated
from uuid import UUID

from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

from app.domain.models.object_id_model import ObjectIdPydanticAnnotation


class MediaBaseModel(BaseModel):
    mongo_id: Annotated[ObjectId, ObjectIdPydanticAnnotation]
    storage_id: Annotated[ObjectId, ObjectIdPydanticAnnotation]


class MediaModel(MediaBaseModel):
    filename: str
    content_type: str
    size: int
    upload_date: datetime = datetime.now()
    metadata: dict = {}
    user_id: str

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True

