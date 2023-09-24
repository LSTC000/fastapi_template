from .models import User

from app.repositories import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
