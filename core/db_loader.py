from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.settings import settings
from src.database.db import ENGINE_ECHO, ENGINE_MAX_OVERFLOW, ENGINE_POOL_SIZE


async_engine = create_async_engine(
    settings.db_url,echo=ENGINE_ECHO, pool_size=ENGINE_POOL_SIZE, max_overflow=ENGINE_MAX_OVERFLOW
)

async_session_maker = async_sessionmaker(async_engine, 
                                         expire_on_commit=False, 
                                         autocommit=False, 
                                         class_=AsyncSession
                                         )


def connection(func):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            return await func(session, *args, **kwargs)

    return wrapper
