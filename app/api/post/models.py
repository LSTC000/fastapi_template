from typing import TYPE_CHECKING

from app.db import Base

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


if TYPE_CHECKING:
    from app.api.user.models import User


class Post(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False, default='')
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user: Mapped['User'] = relationship(back_populates='posts')
