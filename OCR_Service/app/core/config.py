from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    TESSERACT_CMD: str
    MEDIA_SERVICE_GRPC: str
    IAM_SERVICE_URL: str

    model_config = SettingsConfigDict(env_file="app/.env")


@lru_cache
def get_settings():
    return Settings()
