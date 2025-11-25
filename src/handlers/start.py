from aiogram.types import Message

from core.app import dp
from src.database.tasks.check import set_user, get_user
import src.keyboards.main as main_kb
import messages as msg_text


@dp.message_handler(commands=["start"])
async def start(msg: Message):
    user, ban = await get_user(msg.from_user.id)

    if not user:
        user_lang = msg.from_user.language_code
        if user_lang not in ["ru", "es"]:
            user_lang = "en"
        
        user = await set_user(msg.from_user.id, msg.from_user.username, user_lang)

    if ban:
        await msg.answer("Вы в бане")
        return
    
    if user.is_admin:
        await msg.answer(msg_text.start_mes_ru, reply_markup=main_kb.main_menu_admin)
    else:
        if user.language == "ru":
            await msg.answer(msg_text.start_mes_ru, reply_markup=main_kb.main_menu_ru)
        elif user.language == "es":
            await msg.answer(msg_text.start_mes_es, reply_markup=main_kb.main_menu_es)
        else:
            await msg.answer(msg_text.start_mes_en, reply_markup=main_kb.main_menu_en)
