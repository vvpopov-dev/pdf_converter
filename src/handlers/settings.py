from aiogram.types import CallbackQuery

from core.app import dp
from src.database.tasks.check import get_user, update_language
import src.keyboards.main as main_kb
import messages as msg_text


# @dp.callback_query_handler(lambda setting: 
#                     setting.data == "set_btn_ru" or 
#                     setting.data == "set_btn_en" or 
#                     setting.data == "set_btn_es"
#                     )
# async def settings(call: CallbackQuery):
#     user = await get_user(call.from_user.id)
#     # print(user[0])

#     if user.language == "ru":
#         await call.message.edit_text(msg_text.settings_mes_ru, reply_markup=main_kb.settings_menu_ru)
#     elif user.language == "es":
#         await call.message.edit_text(msg_text.settings_mes_es, reply_markup=main_kb.settings_menu_es)
#     else:
#         await call.message.edit_text(msg_text.settings_mes_en, reply_markup=main_kb.settings_menu_en)


@dp.callback_query_handler(lambda change:
                           change.data == "chg_btn_ru" or
                           change.data == "chg_btn_en" or
                           change.data == "chg_btn_es"
                           )
async def change_language(call: CallbackQuery):
    user = await get_user(call.from_user.id)

    if user.language == "ru":
        await call.message.edit_text(msg_text.change_lang_mes_ru, reply_markup=main_kb.language_menu)
    elif user.language == "es":
        await call.message.edit_text(msg_text.change_lang_mes_es, reply_markup=main_kb.language_menu)
    else:
        await call.message.edit_text(msg_text.change_lang_mes_en, reply_markup=main_kb.language_menu)


@dp.callback_query_handler(lambda lang:
                           lang.data == "lang_btn_ru" or
                           lang.data == "lang_btn_en" or
                           lang.data == "lang_btn_es"
                           )
async def set_language(call: CallbackQuery):
    try:
        await update_language(call.from_user.id, new_language=user_lang)

        if call.data == "lang_btn_ru":
            user_lang = "ru"
            await call.message.edit_text(msg_text.set_lang_ru, reply_markup=main_kb.main_menu_ru)
        elif call.data == "lang_btn_es":
            user_lang = "es"
            await call.message.edit_text(msg_text.set_lang_es, reply_markup=main_kb.main_menu_es)
        else:
            user_lang = "en"
            await call.message.edit_text(msg_text.set_lang_en, reply_markup=main_kb.main_menu_en)
    except:
        await call.message.edit_text(msg_text.error_en, )