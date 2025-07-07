import asyncio
import secrets
import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated, Any

from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import PlainTextResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from loguru import logger
from prometheus_client import CollectorRegistry, generate_latest, multiprocess
from psutil import cpu_percent, virtual_memory  # type: ignore

from nginx_fastapi.core.logger import init_logger
from nginx_fastapi.core.settings import get_settings
from nginx_fastapi.metrics import (
    CPU_USAGE,
    MEMORY_USAGE,
    REQUEST_COUNT,
    REQUEST_LATENCY,
    REQUESTS_IN_PROGRESS,
)

auth_scheme = HTTPBasic()


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


@app.middleware("http")
async def request_interceptor(request: Request, call_next: Any) -> Response:

    REQUESTS_IN_PROGRESS.labels(
        method=request.method,
        endpoint=request.url.path,
    ).inc()

    start_time = time.perf_counter()
    response: Response = await call_next(request)
    process_time = time.perf_counter() - start_time

    REQUESTS_IN_PROGRESS.labels(
        method=request.method,
        endpoint=request.url.path,
    ).dec()

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status_code=response.status_code,
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.url.path,
        status_code=response.status_code,
    ).observe(process_time)

    return response


@app.get("/metrics", response_class=PlainTextResponse)
async def metrics(
    credentials: Annotated[HTTPBasicCredentials, Depends(auth_scheme)],
) -> bytes:
    """
    Expose the metrics endpoint for Prometheus to scrape.
    """

    settings = get_settings()

    compared_username = secrets.compare_digest(
        credentials.username.encode("utf8"),
        settings.API_METRICS_USERNAME.encode("utf8"),
    )
    compared_password = secrets.compare_digest(
        credentials.password.encode("utf8"),
        settings.API_METRICS_PASSWORD.encode("utf8"),
    )

    if not (compared_username and compared_password):
        logger.warning("Unauthorized access attempt to /metrics endpoint.")
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)

    cpu_task = asyncio.to_thread(cpu_percent, interval=0.1)
    memory_task = asyncio.to_thread(virtual_memory)

    cpu_usage, memory_usage = await asyncio.gather(cpu_task, memory_task)

    CPU_USAGE.set(cpu_usage)
    MEMORY_USAGE.set(memory_usage.percent)

    return generate_latest(registry)
