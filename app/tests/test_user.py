from .conftest import async_session_maker

from app.api.user.models import User

from sqlalchemy import insert


async def test_add():
    async with async_session_maker() as session:
        stmt = insert(User).values(name='ivan', surname='ivanov', email='user1@example.com', is_active=True)
        await session.execute(stmt)
        await session.commit()
