from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from core.app import dp
from src.database.tasks.check import get_user
import src.keyboards.main as main_kb
import messages as msg_text


@dp.callback_query_handler(lambda back: 
                    back.data == "back_btn_ru" or 
                    back.data == "back_btn_en" or 
                    back.data == "back_btn_es",
                    state="*"
                    )
async def back_to_main(call: CallbackQuery, state: FSMContext):
    await state.finish()
    user = await get_user(call.from_user.id)
    if user.is_admin == "true":
        await call.message.edit_text(msg_text.main_mes_ru, reply_markup=main_kb.main_admin)
    else:
        if user.language == "ru":
            await call.message.edit_text(msg_text.main_mes_ru, reply_markup=main_kb.main_menu_ru)
        elif user.language == "es":
            await call.message.edit_text(msg_text.main_mes_es, reply_markup=main_kb.main_menu_es)
        else:
            await call.message.edit_text(msg_text.main_mes_en, reply_markup=main_kb.main_menu_en)
