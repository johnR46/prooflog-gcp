import logging

import uvicorn
from fastapi import FastAPI
from fastapi.logger import logger

from apis import proof_concept_log
from cloud_logging.middleware import LoggingMiddleware
from cloud_logging.setup import setup_logging
from settings import environment

app = FastAPI()
app.include_router(proof_concept_log.router)

if environment == 'production':
    setup_logging()
    app.add_middleware(LoggingMiddleware)
else:
    logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True, debug=False)
