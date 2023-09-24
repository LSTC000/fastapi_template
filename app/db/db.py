from typing import AsyncGenerator

from app.common import config

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(
    f'postgresql+asyncpg://{config.db_user}:{config.db_pass}@{config.db_host}:{config.db_port}/{config.db_name}'
)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
