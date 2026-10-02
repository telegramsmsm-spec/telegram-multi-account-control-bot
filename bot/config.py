from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import List, Union

class Settings(BaseSettings):
    bot_token: str
    api_id: int
    api_hash: str
    admin_ids: List[int] = []
    database_url: str = "sqlite+aiosqlite:///./data/bot.db"
    default_delay_min: int = 3
    default_delay_max: int = 8

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @field_validator("admin_ids", mode="before")
    @classmethod
    def parse_admin_ids(cls, v):
        if v is None or v == "":
            return []
        if isinstance(v, int):
            return [v]
        if isinstance(v, list):
            return [int(x) for x in v]
        # handle string from .env like "123" or "123,456"
        if isinstance(v, str):
            parts = [p.strip() for p in v.split(",") if p.strip()]
            return [int(p) for p in parts]
        return [int(v)]

settings = Settings()
