from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    bot_token: str
    api_id: int
    api_hash: str
    admin_ids: List[int] = []          # Only these IDs can use the bot
    database_url: str = "sqlite+aiosqlite:///./data/bot.db"
    default_delay_min: int = 3
    default_delay_max: int = 8

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
