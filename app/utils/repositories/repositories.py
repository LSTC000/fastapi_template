from abc import ABC, abstractmethod

from app.db import async_session_maker

from sqlalchemy import insert, select, update, delete
from sqlalchemy.engine import Result
from sqlalchemy.orm import QueryableAttribute, strategy_options


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, target_data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_one(
            self,
            target_id: int,
            option: strategy_options = None,
            queryable_attribute: QueryableAttribute = None
    ):
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
            response: Result = await session.execute(stmt)
            await session.commit()

        return response.scalar_one_or_none()

    async def get_one(
            self,
            target_id: int,
            option: strategy_options = None,
            queryable_attribute: QueryableAttribute = None
    ) -> dict | None:
        async with async_session_maker() as session:
            if option is not None and queryable_attribute is not None:
                query = select(self.model).options(option(queryable_attribute)).where(self.model.id == target_id)
            else:
                query = select(self.model).where(self.model.id == target_id)

            response: Result = await session.scalars(query)
            response_data = response.first()

        return response_data.__dict__ if response_data is not None else response_data

    async def edit_one(self, target_id: int, new_target_data: dict) -> int | None:
        async with async_session_maker() as session:
            stmt = update(self.model) \
                .where(self.model.id == target_id) \
                .values(**new_target_data) \
                .returning(self.model.id)
            response: Result = await session.execute(stmt)
            await session.commit()

        return response.scalar_one_or_none()

    async def delete_one(self, target_id: int) -> int | None:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == target_id).returning(self.model.id)
            response: Result = await session.execute(stmt)
            await session.commit()

        return response.scalar_one_or_none()
