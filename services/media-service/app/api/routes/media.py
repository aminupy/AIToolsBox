from typing import Annotated
from loguru import logger
from fastapi import APIRouter, Depends, UploadFile, status, Form
from fastapi.responses import StreamingResponse

from app.domain.schemas.media import MediaRequest, MediaResponse
from app.domain.schemas.token_user import TokenUser
from app.services.media_service import MediaService
from app.api.dependencies.auth import get_current_user

media_router = APIRouter()


@media_router.post(
    "/upload", response_model=MediaResponse, status_code=status.HTTP_201_CREATED
)
async def upload_media(
    upload_file: UploadFile,
    current_user: Annotated[TokenUser, Depends(get_current_user)],
    media_service: Annotated[MediaService, Depends()]
):
    logger.info(f"Uploading media {upload_file.filename}")
    return await media_service.create_media(upload_file, current_user.id)


@media_router.post(
    "/download", response_class=StreamingResponse, status_code=status.HTTP_200_OK
)
async def download_media(
    media_request: MediaRequest,
    current_user: Annotated[TokenUser, Depends(get_current_user)],
    media_service: Annotated[MediaService, Depends()],
):
    media_schema, file_stream = await media_service.get_media(
        media_request.id, current_user.id
    )

    logger.info(f"Downloading file {media_schema.name}")

    return StreamingResponse(
        content=file_stream(),
        media_type=media_schema.content_type,
        headers={
            "Content-Disposition": f"attachment; filename={media_schema.name}"
        },
    )
