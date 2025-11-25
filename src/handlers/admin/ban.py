import re

from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from core.app import dp
from src.database.tasks.admin import ban_user, unban_user
from src.keyboards.main import admin_kb, back_en


class BanStates(StatesGroup):
    waiting_for_ban_id = State()
    waiting_for_ban_reason = State()
    waiting_for_unban_id = State()


@dp.callback_query_handler(lambda ban: ban.data == "ban")
async def ban(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Укажите ID пользователя, которого необходимо заблокировать", reply_markup = back_en)
    await BanStates.waiting_for_ban_id.set()


@dp.message_handler(content_types=ContentType.TEXT, state=BanStates.waiting_for_ban_id)
async def _ban_id(msg: Message, state: FSMContext):
    if re.match(r"\d+", msg.text):
        await state.finish()
        await msg.answer("Укажите причину блокировки", reply_markup = back_en)
        await state.update_data(ban_id = int(msg.text))
        await BanStates.waiting_for_ban_reason.set()
    else:
        await msg.answer("Введите ID пользователя", reply_markup = back_en)


@dp.message_handler(content_types=ContentType.TEXT, state=BanStates.waiting_for_ban_reason)
async def _ban_reason(msg: Message, state: FSMContext):
    try:
        data = await state.get_data()
        ban_id = data.get("ban_id")
        ban_query = await ban_user(tg_id = ban_id, admin_username = msg.from_user.username, reason = msg.text)
    except Exception as e:
        print(e)
    await state.finish()
    if ban_query:
        await msg.answer("Пользователь заблокирован", reply_markup = back_en)


@dp.callback_query_handler(lambda unban: unban.data == "unban")
async def unban(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Укажите ID пользователя, которого необходимо разблокировать", reply_markup = back_en)
    await BanStates.waiting_for_unban_id.set()


@dp.message_handler(content_types=ContentType.TEXT, state=BanStates.waiting_for_unban_id)
async def _unban(msg: Message, state: FSMContext):
    if re.match(r"\d+", msg.text):
        await state.finish()
        unban_query = await unban_user(tg_id = int(msg.text), admin_username = msg.from_user.username)
        if unban_query:
            await msg.answer("Пользователь разблокирован", reply_markup = back_en)
    else:
        await msg.answer("Введите ID пользователя", reply_markup = back_en)
