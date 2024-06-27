from functools import lru_cache
from pathlib import Path
from loguru import logger

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    FILE_STORAGE_PATH: str
    IAM_URL: str
    GRPC_PORT: int

    # model_config = SettingsConfigDict(env_file=str(Path(__file__).resolve().parent / ".env"))


@lru_cache
@logger.catch
def get_settings():
    return Settings()
