from fastapi import FastAPI
import logging
from fastapi.logger import logger

from apis import proof_concept_log
from cloud_logging.middleware import LoggingMiddleware
from cloud_logging.setup import setup_logging
from settings import environment

app = FastAPI(
    title="Proof Log GCP",
    description="Log Risk for GCP",
    debug=False,
    version="0.0.1"
)

if environment == 'production':
    setup_logging()
    app.add_middleware(LoggingMiddleware)
else:
    logger.setLevel(logging.DEBUG)


@app.on_event("startup")
async def startup_event():
    logger.info("Application start")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutdown")


app.include_router(proof_concept_log.router)
