import logging
from fastapi import FastAPI
from fastapi.logger import logger
from pydantic import BaseSettings

from apis import proof_concept_log
from cloud_logging.middleware import LoggingMiddleware
from cloud_logging.setup import setup_logging


class Settings(BaseSettings):
    environment: str = 'production'


settings = Settings()
app = FastAPI()
app.include_router(proof_concept_log.router)

if settings.environment == 'production':
    setup_logging()
    app.add_middleware(LoggingMiddleware)
else:
    logger.setLevel(logging.DEBUG)
