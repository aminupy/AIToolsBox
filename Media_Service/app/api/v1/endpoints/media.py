from uuid import UUID

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status, Form
from fastapi.responses import FileResponse, StreamingResponse
from typing import Annotated

from pydantic import Field

from app.domain.schemas.media_schema import MediaCreateResponseSchema, MediaGetSchema, MediaGetResponseSchema
from app.services.media_service import MediaService


media_router = APIRouter()


@media_router.post("/UploadMedia", response_model=MediaCreateResponseSchema, status_code=status.HTTP_201_CREATED)
async def upload_media(media_service: Annotated[MediaService, Depends()],
                       file: UploadFile, user_id: str = Form(...)):
    media = await media_service.create_media(file, user_id)
    return MediaCreateResponseSchema(media=media, message="Media uploaded successfully")


@media_router.post("/GetMedia", status_code=status.HTTP_200_OK)
async def get_media(media_get: MediaGetSchema, media_service: Annotated[MediaService, Depends()]):
    media, file_stream = await media_service.get_media(media_get.mongo_id)

    return StreamingResponse(content=file_stream(), media_type=media.content_type)