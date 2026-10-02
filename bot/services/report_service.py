"""Internal + External report orchestration"""
from loguru import logger
import asyncio

class ReportService:
    async def internal_report(self, accounts: list, target: str, report_type: str, templates: list):
        logger.info(f"Internal report on {target} with {len(accounts)} accounts")
        for i, acc in enumerate(accounts):
            text = templates[i % len(templates)]
            # TODO: real report action
            logger.info(f"Account {acc} reported {target} with unique text")
            await asyncio.sleep(5)
        logger.info("Internal reports finished")

    async def external_report(self, email_accounts: list, target_address: str, templates: list):
        logger.info(f"External reports to {target_address}")
        for i, email in enumerate(email_accounts):
            text = templates[i % len(templates)]
            # TODO: real SMTP send
            logger.info(f"Email {email} sent report")
            await asyncio.sleep(3)

report_service = ReportService()
