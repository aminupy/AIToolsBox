from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status, Form
from fastapi.responses import StreamingResponse

from app.domain.schemas.media_schema import MediaGetSchema, MediaSchema
from app.services.media_service import MediaService

media_router = APIRouter()


@media_router.post(
    "/UploadMedia", response_model=MediaSchema, status_code=status.HTTP_201_CREATED
)
async def upload_media(
    media_service: Annotated[MediaService, Depends()],
    file: UploadFile,
    user_id: str = Form(...),
):
    return await media_service.create_media(file, user_id)


@media_router.post(
    "/GetMedia", response_class=StreamingResponse, status_code=status.HTTP_200_OK
)
async def get_media(
    media_get: MediaGetSchema, media_service: Annotated[MediaService, Depends()]
):
    media_schema, file_stream = await media_service.get_media(media_get.mongo_id)

    return StreamingResponse(
        content=file_stream(),
        media_type=media_schema.content_type,
        headers={
            "Content-Disposition": f"attachment; filename={media_schema.filename}"
        },
    )
