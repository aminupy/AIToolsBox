from typing import Annotated

from fastapi import APIRouter, Depends, status, Form
from fastapi.responses import StreamingResponse

from app.domain.schemas.ocr_schema import OCRCreateRequest, OCRCreateResponse, OCRRequest, OCRResponse
from app.domain.schemas.token_schema import TokenDataSchema
from app.services.auth_service import get_current_user
from app.services.ocr_service import OCRService

ocr_router = APIRouter()


@ocr_router.post(
    "/process", response_model=OCRCreateResponse, status_code=status.HTTP_201_CREATED
)
async def process_image(
    ocr_create: OCRCreateRequest,
    current_user: Annotated[TokenDataSchema, Depends(get_current_user)],
    ocr_service: Annotated[OCRService, Depends()]
):
    return await ocr_service.process_image(ocr_create, current_user.id)


@ocr_router.post(
    "/get_ocr_result", response_model=OCRResponse, status_code=status.HTTP_200_OK
)
async def get_ocr_result(
    ocr_request: OCRRequest,
    current_user: Annotated[TokenDataSchema, Depends(get_current_user)],
    ocr_service: Annotated[OCRService, Depends()]
):
    return await ocr_service.get_ocr_result(ocr_request, current_user.id)


@ocr_router.get(
    "/get_ocr_history", response_model=list[OCRResponse], status_code=status.HTTP_200_OK
)
async def get_ocr_history(
    current_user: Annotated[TokenDataSchema, Depends(get_current_user)],
    ocr_service: Annotated[OCRService, Depends()]
):
    return await ocr_service.get_ocr_history(current_user.id)