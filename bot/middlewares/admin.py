from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject
from bot.config import settings
from loguru import logger

class AdminOnlyMiddleware(BaseMiddleware):
    """Only users in ADMIN_IDS can use the bot. Everyone else is blocked."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = None
        if isinstance(event, Message):
            user = event.from_user
        elif isinstance(event, CallbackQuery):
            user = event.from_user

        if user is None:
            return await handler(event, data)

        if user.id not in settings.admin_ids:
            logger.warning(f"Blocked non-admin access attempt from {user.id} (@{user.username})")
            if isinstance(event, Message):
                await event.answer("⛔ Access denied.\nThis bot is private. Only the owner can use it.")
            elif isinstance(event, CallbackQuery):
                await event.answer("⛔ Access denied. Owner only.", show_alert=True)
            return  # stop processing

        return await handler(event, data)
