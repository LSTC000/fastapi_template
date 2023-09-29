from datetime import datetime
from typing import TYPE_CHECKING

from app.db import Base

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from app.api.post.models import Post


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    surname: Mapped[str] = mapped_column(String(32), nullable=False)
    email: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    posts: Mapped[list['Post']] = relationship(back_populates='user')
