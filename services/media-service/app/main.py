from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.v1.endpoints.media import media_router
from app.logging_service.logging_config import configure_logger

configure_logger()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(media_router, prefix="/api/v1/media", tags=["media"])

logger.info("Media Service Started")


@app.get("/")
async def root():
    return {"message": "Hello From Media Service !"}
