from aiogram.types import InlineKeyboardButton


"""Ban button"""
ban_btn = InlineKeyboardButton("Заблокировать", callback_data="ban")

"""Unban button"""
unban_btn = InlineKeyboardButton("Разблокировать", callback_data="unban")

"""Send message for all users"""
sendall_btn = InlineKeyboardButton("Отправить рассылку", callback_data="sendall")

"""Statistic button"""
stat_btn = InlineKeyboardButton("Показать статистику бота", callback_data="stat")

"""Admin menu"""
adm_menu_btn = InlineKeyboardButton("Перейти в админ-панель", callback_data="adm_menu")

"""Add admin"""
adm_add_btn = InlineKeyboardButton("Добавить администратора", callback_data="adm_add")

"""Delete admin"""
adm_del_btn = InlineKeyboardButton("Удалить администратора", callback_data="adm_del")