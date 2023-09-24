from .repositories import UserRepository
from .services import UserService


def user_service():
    return UserService(UserRepository)
