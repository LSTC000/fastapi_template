from .repositories import UserRepository
from .services import UserDBService, UserEmailService


def user_db_service():
    return UserDBService(UserRepository)


def user_email_service():
    return UserEmailService
