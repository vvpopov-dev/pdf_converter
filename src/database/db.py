from sqlalchemy.orm import DeclarativeBase


ENGINE_POOL_SIZE = 50
ENGINE_MAX_OVERFLOW = 10
ENGINE_ECHO = False


class Base(DeclarativeBase):
    pass
