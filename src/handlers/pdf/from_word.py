from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup

from core.app import dp
from src.database.tasks.check import get_user

import src.keyboards.main as main_kb
import messages as msg_text


@dp.callback_query_handler(lambda word: 
                           word.data == "word_btn_ru" or 
                           word.data == "word_btn_en" or 
                           word.data == "word_btn_es")
async def word_to_pdf_handler(call: CallbackQuery):
    user, ban = await get_user(call.from_user.id)

    if ban:
        await call.message.edit_text("Вы в бане")
        return

    if user.language == "ru":
        await call.message.edit_text(msg_text.out_of_ord_mes_ru, reply_markup=main_kb.back_ru)
    elif user.language == "es":
        await call.message.edit_text(msg_text.out_of_ord_mes_es, reply_markup=main_kb.back_es)
    else:
        await call.message.edit_text(msg_text.out_of_ord_mes_en, reply_markup=main_kb.back_en)
