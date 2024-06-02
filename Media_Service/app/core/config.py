from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    FILE_STORAGE_PATH: str

    model_config = SettingsConfigDict(env_file='app/.env')


@lru_cache
def get_settings():
    return Settings()
