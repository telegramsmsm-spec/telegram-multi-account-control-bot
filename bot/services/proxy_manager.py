"""Proxy health and assignment"""
from loguru import logger

class ProxyManager:
    async def check_proxy(self, proxy: dict) -> bool:
        # TODO: real connectivity test to Telegram DC
        logger.info(f"Checking proxy {proxy.get('host')}:{proxy.get('port')}")
        return True

    async def assign_proxy(self, account_id: int, proxy_id: int):
        logger.info(f"Assigned proxy {proxy_id} to account {account_id}")

proxy_manager = ProxyManager()
