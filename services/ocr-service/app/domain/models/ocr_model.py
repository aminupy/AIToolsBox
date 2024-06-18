from datetime import datetime


from pydantic import BaseModel
from app.domain.models.object_id_model import ObjectIdPydanticAnnotation, ObjectId
from typing import Annotated


class OCRModel(BaseModel):
    ocr_id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = None
    image_id: str
    user_id: str
    text: str
    created_at: datetime = datetime.now()

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: str
        }