from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, status, Form
from fastapi.responses import StreamingResponse

from app.domain.schemas.media_schema import MediaGetSchema, MediaSchema
from app.domain.schemas.token_schema import TokenDataSchema
from app.services.media_service import MediaService
from app.services.auth_service import get_current_user

media_router = APIRouter()


@media_router.post(
    "/UploadMedia", response_model=MediaSchema, status_code=status.HTTP_201_CREATED
)
async def upload_media(
    media_service: Annotated[MediaService, Depends()],
    file: UploadFile,
    current_user: Annotated[TokenDataSchema, Depends(get_current_user)],
):
    return await media_service.create_media(file, current_user.id)


@media_router.post(
    "/GetMedia", response_class=StreamingResponse, status_code=status.HTTP_200_OK
)
async def get_media(
    media_get: MediaGetSchema,
    media_service: Annotated[MediaService, Depends()],
    current_user: Annotated[TokenDataSchema, Depends(get_current_user)],
):
    media_schema, file_stream = await media_service.get_media(
        media_get.mongo_id, current_user.id
    )

    return StreamingResponse(
        content=file_stream(),
        media_type=media_schema.content_type,
        headers={
            "Content-Disposition": f"attachment; filename={media_schema.filename}"
        },
    )
