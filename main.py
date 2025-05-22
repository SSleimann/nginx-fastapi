from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from nginx_fastapi.core.logger import init_logger
from nginx_fastapi.core.settings import get_settings


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting FastAPI application...")

    settings = get_settings()
    init_logger(settings)

    yield

    logger.info("Stopping FastAPI application...")


app = FastAPI(
    title="FastAPI Example",
    description="A simple FastAPI application to demonstrate the use of FastAPI, Nginx and Prometheus.",
    version="1.0.0",
    lifespan=lifespan,
)
