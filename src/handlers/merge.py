from io import BytesIO
import asyncio

from aiogram import types
from aiogram.types import ContentType, Document, Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from core.app import dp, bot
from src.service.merge import merge_pdf
import src.keyboards.main as main_kb
import messages as msg_text
from src.database.tasks.check import get_user


class MergeStates(StatesGroup):
    waiting_for_files = State()


media_groups = {}
wait_messages = {}


@dp.callback_query_handler(lambda c: 
                           c.data == "merge_btn_en" or 
                           c.data == "merge_btn_ru" or 
                           c.data == "merge_btn_es")
async def merge_pdf_handler(call: types.CallbackQuery, state: FSMContext):
    user = await get_user(call.from_user.id)
    if user.language == "ru":
        msg = await call.message.edit_text(msg_text.merge_mes_ru, reply_markup=main_kb.back_ru)
    elif user.language == "es":
        msg = await call.message.edit_text(msg_text.merge_mes_es, reply_markup=main_kb.back_es)
    else:
        msg = await call.message.edit_text(msg_text.merge_mes_en, reply_markup=main_kb.back_en)
    
    await state.update_data(start_message_id=msg.message_id)

    await MergeStates.waiting_for_files.set()


@dp.message_handler(content_types=ContentType.DOCUMENT, state=MergeStates.waiting_for_files)
async def _merge_pdf_handler(msg: Message, state: FSMContext):
    data = await state.get_data()
    start_message_id = data.get("start_message_id")
    if start_message_id:
        try:
            await bot.delete_message(msg.chat.id, start_message_id)
        except Exception:
            pass

    user = await get_user(msg.from_user.id)
    if msg.document.mime_type != "application/pdf":
        await state.finish()
        if user.language == "ru":
            await msg.answer(msg_text.merge_mes_ru, reply_markup=main_kb.back_ru)
        elif user.language == "es":
            await msg.answer(msg_text.merge_mes_es, reply_markup=main_kb.back_es)
        else:
            await msg.answer(msg_text.merge_mes_en, reply_markup=main_kb.back_en)
        
        await MergeStates.waiting_for_files.set()
        return

    if not msg.media_group_id:
        await state.finish()
        if user.language == "ru":
            await msg.answer(msg_text.merge_mes_ru, reply_markup=main_kb.back_ru)
        elif user.language == "es":
            await msg.answer(msg_text.merge_mes_es, reply_markup=main_kb.back_es)
        else:
            await msg.answer(msg_text.merge_mes_en, reply_markup=main_kb.back_en)

        await MergeStates.waiting_for_files.set()
        return

    group_id = msg.media_group_id

    if group_id not in media_groups:
        media_groups[group_id] = []
        if user.language == "ru":
            wait_msg = await msg.answer(msg_text.wait_mes_ru)
        elif user.language == "es":
            wait_msg = await msg.answer(msg_text.wait_mes_es)
        else:
            wait_msg = await msg.answer(msg_text.wait_mes_en)
        wait_messages[group_id] = wait_msg.message_id

    media_groups[group_id].append(msg)

    await asyncio.sleep(1)

    if group_id in media_groups:
        messages = media_groups.pop(group_id)
        pdf_files = []

        for file in messages:
            get_file = await file.document.get_file()
            byte_io = BytesIO()
            await bot.download_file(get_file.file_path, byte_io)
            byte_io.seek(0)
            pdf_files.append(byte_io)

        pdf = merge_pdf(*pdf_files, user_id=msg.from_user.id)
        pdf.name = f"{msg.from_user.username}-merged.pdf"

        if group_id in wait_messages:
            try:
                await bot.delete_message(msg.chat.id, wait_messages[group_id])
            except Exception:
                pass
            wait_messages.pop(group_id, None)

        # await msg.edit_text(msg.from_user.id, "Ваш файл готов!", reply_markup=main_kb.main_menu_ru)
        await bot.send_document(document=pdf, chat_id=msg.chat.id)
        
        await msg.answer(msg_text.cmpl_mes_ru if user.language == "ru" 
                         else msg_text.cmpl_mes_es if user.language == "es" 
                         else msg_text.cmpl_mes_en, 
                         reply_markup=main_kb.main_menu_ru if user.language == "ru" 
                         else main_kb.main_menu_es if user.language == "es" 
                         else main_kb.main_menu_en
                         )

        

        await state.finish()    
