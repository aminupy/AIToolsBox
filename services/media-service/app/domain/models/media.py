from datetime import datetime
from typing import Annotated
from uuid import UUID
from bson import ObjectId
from pydantic import BaseModel

from app.domain.models.object_id import ObjectIdPydanticAnnotation


class MediaModel(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = None
    name: str
    type: str
    size: int
    metadata: dict = {}
    user_id: str
    upload_date: datetime = datetime.now()


class MediaGridFSModel(MediaModel):
    storage_id: Annotated[ObjectId, ObjectIdPydanticAnnotation]

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True
