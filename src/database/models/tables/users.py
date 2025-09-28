from sqlalchemy import BigInteger

from sqlalchemy.orm import Mapped, mapped_column
from src.database.db import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(nullable=False, type_=BigInteger, unique=True)
    tg_username: Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(nullable=True)
    language: Mapped[str] = mapped_column(default='en')
