from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Enviroments(str, Enum):
    DEV = "dev"
    TESTING = "testing"
    PROD = "prod"


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Environment
    ENV: Enviroments = Enviroments.DEV

    # Metrics Authentication
    API_METRICS_USERNAME: str = "admin"
    API_METRICS_PASSWORD: str = "admin"


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
