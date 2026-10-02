from loguru import logger
import sys

logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add("data/logs/bot_{time}.log", rotation="10 MB", retention="7 days", level="DEBUG")
