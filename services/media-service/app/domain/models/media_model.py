from datetime import datetime
from typing import Annotated
from uuid import UUID

from bson import ObjectId
from pydantic import BaseModel

from app.domain.models.object_id_model import ObjectIdPydanticAnnotation


class MediaModel(BaseModel):
    mongo_id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = None
    filename: str
    content_type: str
    size: int
    upload_date: datetime = datetime.now()
    metadata: dict = {}
    user_id: str


class MediaGridFSModel(MediaModel):
    storage_id: Annotated[ObjectId, ObjectIdPydanticAnnotation]

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True
