from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.db import init_db
from app.api import auth_router
from app.core.logging.logger import configure_logger
from app.core.config import get_settings

config = get_settings()
configure_logger()
init_db()
app = FastAPI(title=config.APP_NAME, version=config.APP_VERSION)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])

logger.info("IAM Service Started")


@app.get("/")
async def root():
    return {"message": "Hello from IAM Service !"}
