from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup

from core.app import dp, bot
from src.database.tasks.check import get_user, update_language
from core.settings import settings

import src.keyboards.main as main_kb
import messages as msg_text


class SupportStates(StatesGroup):
    waiting_for_files = State()


@dp.callback_query_handler(lambda sup:
                           sup.data == "help_btn_ru" or
                           sup.data == "help_btn_en" or
                           sup.data == "help_btn_es"
                           )
async def support(call: CallbackQuery):
    user = await get_user(call.from_user.id)

    if user.language == "ru":
        await call.message.edit_text(msg_text.support_mes_ru, reply_markup=main_kb.back_ru)
    elif user.language == "es":
        await call.message.edit_text(msg_text.support_mes_es, reply_markup=main_kb.back_es)
    else:
        await call.message.edit_text(msg_text.support_mes_en, reply_markup=main_kb.back_en)

    await SupportStates.waiting_for_files.set()

@dp.message_handler(content_types=["text"], state=SupportStates.waiting_for_files)
async def support_message(msg: Message, state):
    user_msg = msg.text
    await bot.send_message(chat_id=settings.ADMIN_ID, text=f"Message from {msg.from_user.id} ({msg.from_user.username}):\n{user_msg}")

    user = await get_user(msg.from_user.id)
    if user.language == "ru":
        await msg.answer(msg_text.conf_mes_ru, reply_markup=main_kb.back_ru)
    elif user.language == "es":
        await msg.answer(msg_text.conf_mes_es, reply_markup=main_kb.back_es)
    else:
        await msg.answer(msg_text.conf_mes_en, reply_markup=main_kb.back_en)
    
    await state.finish()