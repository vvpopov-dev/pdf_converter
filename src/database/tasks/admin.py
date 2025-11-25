from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.database.models.tables.banned import Banned
from src.database.tasks.check import get_user
from core.db_loader import connection


@connection
async def ban_user(session, tg_id: int, admin_username: str, reason: str):
    try:
        user = await get_user(tg_id)
        if user:
            new_ban = Banned(user_id=user.id,
                            tg_id=tg_id, 
                            admin_username=admin_username, 
                            reason=reason
                            )
            session.add(new_ban)
            await session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


@connection
async def unban_user(session, tg_id: int, admin_username: str):
    try:
        user_to_unban = await session.scalar(select(Banned).filter_by(tg_id=tg_id))
        await session.delete(user_to_unban)
        await session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    