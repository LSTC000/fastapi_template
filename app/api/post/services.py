from .schemas import PostAddSchema
from .models import Post

from app.utils.repositories import AbstractRepository
from app.utils.email import Email, EmailSchema, EmailMessages
from app.utils.celery import send_log_task

from sqlalchemy.orm import joinedload


class PostDBService:
    def __init__(self, post_repository: type[AbstractRepository]):
        self.post_repository = post_repository()

    async def add_post(self, post_data: PostAddSchema) -> int | None:
        return await self.post_repository.add_one(post_data.model_dump())

    async def get_post(self, post_id: int, user_data: bool = False) -> dict | None:
        if user_data:
            return await self.post_repository.get_one(
                target_id=post_id,
                option=joinedload,
                queryable_attribute=Post.user
            )

        return await self.post_repository.get_one(target_id=post_id)


class PostEmailService:
    @staticmethod
    @send_log_task.task
    def send_error_log(error_log: str) -> None:
        email_schema = EmailSchema()

        Email.send_email(
            email_schema=email_schema,
            message=EmailMessages.error_log_message(subject='POST ERROR LOG', error_log=error_log)
        )
