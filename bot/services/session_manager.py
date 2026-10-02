"""Session Manager - handles Telethon/Pyrogram clients per account"""
from telethon import TelegramClient
from telethon.sessions import StringSession
from bot.config import settings
from loguru import logger

class SessionManager:
    def __init__(self):
        self.clients = {}

    async def get_client(self, account_id: int, session_string: str, proxy: dict = None):
        if account_id in self.clients:
            return self.clients[account_id]

        proxy_tuple = None
        if proxy:
            proxy_tuple = (proxy["type"], proxy["host"], proxy["port"], True, proxy.get("username"), proxy.get("password"))

        client = TelegramClient(
            StringSession(session_string),
            settings.api_id,
            settings.api_hash,
            proxy=proxy_tuple
        )
        await client.connect()
        self.clients[account_id] = client
        return client

    async def disconnect_all(self):
        for client in self.clients.values():
            await client.disconnect()
        self.clients.clear()

session_manager = SessionManager()
