from fastapi import APIRouter
from fastapi.logger import logger

router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"message": "Not found"}}
)


@router.get("/proof")
def proof_logger():
    logger.debug('DEBUG LOG')
    logger.error('ERROR LOG')
    logger.warning('WARNING LOG')
    logger.info('INFO LOG')
    logger.info('INFO LOG1')
    logger.info('INFO LOG2')
    return {'message': 'Hello World'}
