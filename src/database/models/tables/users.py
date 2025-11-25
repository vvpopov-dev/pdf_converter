from typing import TYPE_CHECKING
from sqlalchemy import BigInteger, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.db import Base


if TYPE_CHECKING:
    from src.database.models.tables.banned import Banned


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False, type_=BigInteger, unique=True)
    tg_username: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_banned: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_admin: Mapped[bool] = mapped_column(nullable=True)
    language: Mapped[str] = mapped_column(default='en')
