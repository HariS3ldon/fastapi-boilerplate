from contextlib import asynccontextmanager
from fastapi import FastAPI


from dotenv import load_dotenv
from config.db import engine, Base
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Database initialization will be handled by Alembic migrations
    yield

app = FastAPI(lifespan=lifespan)


from ms_boilerplate.exception_handlers import register_exception_handlers
register_exception_handlers(app)