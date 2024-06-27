from datetime import datetime
from typing import Annotated

from bson import ObjectId
from pydantic import BaseModel

from app.domain.models.media_model import MediaModel
from app.domain.models.object_id_model import ObjectIdPydanticAnnotation


class MediaSchema(MediaModel):
    message: str

    class Config:
        from_attributes = True
        json_encoders = {ObjectId: str, datetime: lambda v: v.isoformat()}
        arbitrary_types_allowed = True


class MediaGetSchema(BaseModel):
    mongo_id: Annotated[ObjectId, ObjectIdPydanticAnnotation]
    # mongo_id: str
