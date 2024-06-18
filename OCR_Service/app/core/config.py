from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    TESSERACT_CMD: str
    MEDIA_SERVICE_GRPC: str
    IAM_URL: str

    model_config = SettingsConfigDict(env_file=str(Path(__file__).resolve().parent / ".env"))


@lru_cache
def get_settings():
    return Settings()
