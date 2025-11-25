from aiogram.types import CallbackQuery

from core.app import dp
from src.database.tasks.check import get_user
from src.keyboards.main import admin_kb


@dp.callback_query_handler(lambda menu: menu.data == "adm_menu")
async def admin_menu(call: CallbackQuery):
    user = await get_user(call.from_user.id)
    if user.is_admin:
        await call.message.edit_text("Административная панель", reply_markup = admin_kb)
