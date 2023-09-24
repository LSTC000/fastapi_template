from abc import ABC, abstractmethod

from app.db import async_session_maker

from sqlalchemy import insert, select, update, delete


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, target_data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, target_id: int):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self, target_id: int, new_target_data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, target_id: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, target_data: dict) -> int | None:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**target_data).returning(self.model.id)
            response = await session.execute(stmt)
            await session.commit()

        return response.scalar_one_or_none()

    async def get_one(self, target_id: int) -> dict | None:
        async with async_session_maker() as session:
            query = select(self.model).where(self.model.id == target_id)
            response = await session.scalars(query)
            response = response.first()

        return response.__dict__ if response is not None else response

    async def edit_one(self, target_id: int, new_target_data: dict) -> int | None:
        async with async_session_maker() as session:
            stmt = update(self.model) \
                .where(self.model.id == target_id) \
                .values(**new_target_data) \
                .returning(self.model.id)
            response = await session.execute(stmt)
            await session.commit()

        return response.scalar_one_or_none()

    async def delete_one(self, target_id: int) -> int | None:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == target_id).returning(self.model.id)
            response = await session.execute(stmt)
            await session.commit()

        return response.scalar_one_or_none()
