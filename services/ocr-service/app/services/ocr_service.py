import pytesseract
from PIL import Image
from io import BytesIO
from datetime import datetime

from bson import ObjectId
from fastapi import Depends, HTTPException, status
from typing import Annotated, Generator, Callable, Any

from app.infrastructure.repositories.ocr_repository import OCRRepository
from app.infrastructure.clients.media_client import MediaClient

from app.domain.models.ocr_model import OCRModel
from app.domain.schemas.ocr_schema import OCRResponse, OCRRequest, OCRCreateRequest, OCRCreateResponse


class OCRService:
    def __init__(self,
                 ocr_repository: Annotated[OCRRepository, Depends()],
                 media_client: Annotated[MediaClient, Depends()]
                 ):
        self.ocr_repository = ocr_repository
        self.media_client = media_client

    async def process_image(self, ocr_create: OCRCreateRequest, user_id: str) -> OCRCreateResponse:
        image_data = await self.media_client.request_media(ocr_create.image_id, 'image', user_id)
        image = Image.open(BytesIO(image_data))
        extracted_text = pytesseract.image_to_string(image)

        ocr_result = OCRModel(
            image_id=ocr_create.image_id,
            user_id=user_id,
            text=extracted_text
        )
        ocr_model = await self.ocr_repository.create_ocr(ocr_result)
        return OCRCreateResponse(**ocr_model.dict())

    async def get_ocr_result(self, ocr_request: OCRRequest, user_id: str) -> OCRResponse:
        ocr = await self.ocr_repository.get_ocr(ocr_request.ocr_id)
        if not ocr:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OCR not found")
        if ocr.user_id != user_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="User does not have permission to access this OCR")
        return OCRResponse(**ocr.dict())

    async def get_ocr_history(self, user_id: str) -> list[OCRResponse]:
        ocrs = await self.ocr_repository.get_ocr_history(user_id)

        async def map_ocr(ocr: dict) -> OCRResponse:
            return OCRResponse(
                ocr_id=ocr['_id'],
                image_id=ocr['image_id'],
                user_id=ocr['user_id'],
                text=ocr['text'],
                created_at=ocr['created_at']
            )

        return [await map_ocr(ocr) async for ocr in ocrs]
