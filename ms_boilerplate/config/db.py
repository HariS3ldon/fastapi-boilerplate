from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from os import getenv
# Postgres (change creds/db as needed)
databaseUrl = f"postgresql+asyncpg://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}:{getenv('DB_PORT', 5432)}/{getenv('DB_NAME')}"

engine = create_async_engine(databaseUrl, echo=True, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_session() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        yield session
