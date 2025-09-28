from aiogram.types import CallbackQuery

from core.app import dp
from src.keyboards.main import admin_kb


@dp.callback_query_handler(lambda ban: ban.data == "ban")
async def ban(call: CallbackQuery):
    await call.answer("Укажите id кого надо заблокировать", reply_markup = admin_kb)
