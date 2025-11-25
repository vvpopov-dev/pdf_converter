from typing import TYPE_CHECKING
from sqlalchemy import BigInteger, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.db import Base


if TYPE_CHECKING:
    from src.database.models.tables.users import User


class Banned(Base):
    __tablename__ = 'banned'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False, type_=BigInteger, unique=True)
    tg_username: Mapped[str] = mapped_column(nullable=True)
    admin_username: Mapped[str] = mapped_column(nullable=True)
    reason: Mapped[str] = mapped_column(nullable=True) 
