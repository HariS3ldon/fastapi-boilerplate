from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routing.v1 import router as v1_router


from dotenv import load_dotenv
from ms_boilerplate.config.db import engine, Base
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)


from ms_boilerplate.exception_handlers import register_exception_handlers
register_exception_handlers(app)
app.include_router(v1_router, prefix="/v1", tags=["v1"])

    