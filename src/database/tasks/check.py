import logging

from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.database.models.tables.users import User
from core.db_loader import connection


@connection
async def set_user(session, tg_id: int, tg_username: str, language: str) -> Optional[User]:
    try:
        user = await session.scalar(select(User).filter_by(tg_id=tg_id))

        if not user:
            new_user = User(tg_id=tg_id, tg_username=tg_username, language=language, is_active=True)
            session.add(new_user)
            await session.commit()
            logging.INFO(f"Зарегистрировал пользователя с ID {tg_id}!")
            return new_user
        else:
            logging.INFO(f"Пользователь с ID {tg_id} найден!")
            return user
    except SQLAlchemyError as e:
        logging.INFO(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()


@connection
async def get_user(session, tg_id: int) -> Optional[User]:
    try:
        user = await session.scalar(select(User).filter_by(tg_id=tg_id))
        
        if user:
            logging.INFO(f"Пользователь с ID {tg_id} найден!")
            return user
        else:
            logging.INFO(f"Пользователь с ID {tg_id} не найден!")
            return None
    except SQLAlchemyError as e:
        logging.INFO(f"Ошибка при получении пользователя: {e}")
        await session.rollback()
        return None
    

@connection
async def update_language(session, tg_id: int, new_language: str) -> bool:
    try:
        user = await session.scalar(select(User).filter_by(tg_id=tg_id))
        
        if user:
            user.language = new_language
            await session.commit()
            logging.INFO(f"Обновил язык пользователя с ID {tg_id} на {new_language}!")
            return True
        else:
            logging.INFO(f"Пользователь с ID {tg_id} не найден!")
            return False
    except SQLAlchemyError as e:
        logging.INFO(f"Ошибка при обновлении языка пользователя: {e}")
        await session.rollback()
        return False


# @connection
# async def del_user(session, tg_id: int) -> bool:
#     try:
#         user = await session.scalar(select(User).filter_by(id=tg_id))
#         if user:
#             await session.delete(user)
#             await session.commit()
#             print(f"Удалил пользователя с ID {tg_id}!")
#             return True
#         else:
#             print(f"Пользователь с ID {tg_id} не найден!")
#             return False
#     except SQLAlchemyError as e:
#         print(f"Ошибка при удалении пользователя: {e}")
#         await session.rollback()
#         return False