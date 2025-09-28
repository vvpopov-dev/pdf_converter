from aiogram.types import InlineKeyboardMarkup

import src.keyboards.buttons as btn
import src.keyboards.admin_btns as admbtn

"""Главное меню на русском языке"""
main_menu_ru = InlineKeyboardMarkup().add(
    btn.pdf_button_ru, btn.word_button_ru).add(
        btn.merge_button_ru).add(
    btn.help_button_ru, btn.change_lang_button_ru
)

"""Главное меню на английском языке"""
main_menu_en = InlineKeyboardMarkup().add(
    btn.pdf_button_en, btn.word_button_en).add(
        btn.merge_button_en).add(
    btn.help_button_en, btn.change_lang_button_en
)  

"""Главное меню на испанском языке"""
main_menu_es = InlineKeyboardMarkup(row_width=2).add(
    btn.pdf_button_es, btn.word_button_es).add(
        btn.merge_button_es).add(
    btn.help_button_es, btn.change_lang_button_es
)

"""Меню настроек на русском языке"""
settings_menu_ru = InlineKeyboardMarkup(row_width=1).add(
    btn.change_lang_button_ru,
    btn.back_button_ru
)

"""Меню настроек на английском языке"""
settings_menu_en = InlineKeyboardMarkup(row_width=1).add(
    btn.change_lang_button_en,
    btn.back_button_en
)

"""Меню настроек на испанском языке"""
settings_menu_es = InlineKeyboardMarkup(row_width=1).add(
    btn.change_lang_button_es,
    btn.back_button_es
)   

"""Меню выбора языка на общем языке"""
language_menu = InlineKeyboardMarkup(row_width=1).add(
    btn.lang_button_ru,
    btn.lang_button_en,
    btn.lang_button_es,
    btn.back_button_en
)

"""Меню работы с документами на русском языке"""
back_ru = InlineKeyboardMarkup(row_width=1).add(
    btn.back_button_ru
)

"""Меню работы с документами на английском языке"""
back_en = InlineKeyboardMarkup(row_width=1).add(
    btn.back_button_en
)

"""Меню работы с документами на испанском языке"""
back_es = InlineKeyboardMarkup(row_width=1).add(
    btn.back_button_es
)


'''АДМИНИСТРАТИВНАЯ ПАНЕЛЬ'''
admin_kb = InlineKeyboardMarkup(row_width=2).add(
    admbtn.sendall_btn
    ).add(
    admbtn.ban_btn, admbtn.unban_btn, admbtn.stat_btn
)
main_admin = InlineKeyboardMarkup().add(
    btn.pdf_button_ru, btn.word_button_ru).add(
        btn.merge_button_ru).add(
    btn.help_button_ru, btn.change_lang_button_ru, admbtn.adm_menu_btn
)
