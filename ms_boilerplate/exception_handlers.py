from math import log
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, OperationalError
from os import makedirs
import logging
import re

makedirs("var/log", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    filename='var/log/app.log',
    format='%(asctime)s %(levelname)s %(name)s %(message)s [%(endpoint)s]'
)
logger = logging.getLogger(__name__)

async def integrity_error_handler(request, exc: IntegrityError):
    error_msg = str(exc.orig) if hasattr(exc, 'orig') else str(exc)
    match = re.search(r'Key \((\w+)\)', error_msg)
    field = match.group(1) if match else "unknown"
    message = f"{field} already taken"
    logging.error(message)
    return JSONResponse(status_code=409, content={"detail": message})

async def operational_error_handler(request, exc: OperationalError):
    return JSONResponse(status_code=500, content={"detail": "Database connection error"})

async def error_handler(request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "An unexpected error occurred"})


def register_exception_handlers(app):
    app.add_exception_handler(IntegrityError, integrity_error_handler)
    app.add_exception_handler(OperationalError, operational_error_handler)
