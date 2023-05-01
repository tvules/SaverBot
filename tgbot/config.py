from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings, SecretStr

BASE_DIR = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    """Application settings."""

    bot_token: SecretStr
    db_url: str = "sqlite+aiosqlite:///db.sqlite3"
    downloads_dir: str | Path = BASE_DIR / "downloads"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    """Get a cached instance of settings."""
    return Settings()
