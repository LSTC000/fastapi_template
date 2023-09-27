from .repositories import UserRepository
from .services import UserService, UserEmailService


def user_service():
    return UserService(UserRepository)


def user_email_service():
    return UserEmailService
