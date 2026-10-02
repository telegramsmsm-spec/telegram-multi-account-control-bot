"""TXT line-by-line messaging service"""
from loguru import logger
import asyncio

class MessagingService:
    async def send_from_txt(self, accounts: list, group: str, lines: list, delay_min: int = 3, delay_max: int = 8):
        logger.info(f"Starting TXT send to {group} with {len(accounts)} accounts, {len(lines)} lines")
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            for acc in accounts:
                # TODO: real send via session_manager
                logger.info(f"Account {acc} sent line {i+1}: {line[:50]}...")
                await asyncio.sleep(delay_min)  # placeholder
        logger.info("TXT send completed")

messaging_service = MessagingService()
