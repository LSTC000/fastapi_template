from .models import User

from app.utils.repositories import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
