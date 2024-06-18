from datetime import datetime

from pydantic import BaseModel
from typing import Annotated
from app.domain.models.object_id_model import ObjectIdPydanticAnnotation, ObjectId
from app.domain.models.ocr_model import OCRModel


class OCRRequest(BaseModel):
    ocr_id: Annotated[ObjectId, ObjectIdPydanticAnnotation]


class OCRResponse(OCRModel):
    pass



class OCRCreateRequest(BaseModel):
    image_id: str

class OCRCreateResponse(OCRModel):
    pass


