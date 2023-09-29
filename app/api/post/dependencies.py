from .repositories import PostRepository
from .services import PostDBService, PostEmailService


def post_db_service():
    return PostDBService(PostRepository)


def post_email_service():
    return PostEmailService
