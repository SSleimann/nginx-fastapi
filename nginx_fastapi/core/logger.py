import sys

from loguru import logger

from nginx_fastapi.core.settings import AppSettings


def init_logger(settings: AppSettings) -> None:
    logger.remove()

    level = "DEBUG" if settings.ENV != "prod" else "INFO"

    logger.add(
        sys.stderr,
        level=level,
    )
    logger.add(
        "logs.log",
        enqueue=True,
        format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
        backtrace=True,
        rotation="1 MB",
        retention="10 days",
    )

    logger.info("Logger initialized.")  # Log initialization message
