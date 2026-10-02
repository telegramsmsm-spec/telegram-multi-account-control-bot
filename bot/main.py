import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.config import settings
from bot.handlers import start, accounts, proxy, join, messaging, reports_internal, reports_external, templates, navigation
from bot.database.db import init_db
from bot.middlewares.admin import AdminOnlyMiddleware
from loguru import logger

async def main():
    await init_db()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=MemoryStorage())

    # Admin-only lock - applied to every update
    dp.message.middleware(AdminOnlyMiddleware())
    dp.callback_query.middleware(AdminOnlyMiddleware())

    dp.include_router(start.router)
    dp.include_router(navigation.router)
    dp.include_router(accounts.router)
    dp.include_router(proxy.router)
    dp.include_router(join.router)
    dp.include_router(messaging.router)
    dp.include_router(reports_internal.router)
    dp.include_router(reports_external.router)
    dp.include_router(templates.router)

    logger.info("Bot started - Admin-only mode active")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
