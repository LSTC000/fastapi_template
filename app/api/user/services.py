from .schemas import UserAddSchema, UserEditSchema

from app.repositories import AbstractRepository


class UserService:
    def __init__(self, user_repository: type[AbstractRepository]):
        self.user_repository = user_repository()

    async def add_user(self, user_data: UserAddSchema) -> int | None:
        return await self.user_repository.add_one(user_data.model_dump())

    async def get_user(self, user_id: int) -> dict | None:
        return await self.user_repository.get_one(user_id)

    async def edit_user(self, user_id: int, new_user_data: UserEditSchema) -> int | None:
        return await self.user_repository.edit_one(target_id=user_id, new_target_data=new_user_data.model_dump())

    async def delete_user(self, user_id: int) -> dict | None:
        return await self.user_repository.delete_one(user_id)
