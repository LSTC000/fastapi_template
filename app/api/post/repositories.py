from .models import Post

from app.utils.repositories import SQLAlchemyRepository


class PostRepository(SQLAlchemyRepository):
    model = Post
