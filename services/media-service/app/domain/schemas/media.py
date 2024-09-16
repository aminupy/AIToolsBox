from datetime import datetime
from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel

from app.domain.models.media import MediaModel
from app.domain.models.object_id import ObjectIdPydanticAnnotation


class MediaRequest(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation]


class MediaResponse(MediaModel):
    message: str

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True

