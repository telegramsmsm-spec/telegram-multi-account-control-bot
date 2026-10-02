import random
import asyncio
from bot.config import settings

async def human_delay(min_s: int = None, max_s: int = None):
    min_s = min_s or settings.default_delay_min
    max_s = max_s or settings.default_delay_max
    delay = random.uniform(min_s, max_s)
    await asyncio.sleep(delay)
    return delay
