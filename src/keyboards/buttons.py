from aiogram.types import InlineKeyboardButton


"""Кнопки конвертации PDF в Word"""
pdf_button_ru = InlineKeyboardButton("📄PDF в Word", callback_data="pdf_btn_ru")
pdf_button_en = InlineKeyboardButton("📄PDF to Word", callback_data="pdf_btn_en")
pdf_button_es = InlineKeyboardButton("📄PDF a Word", callback_data="pdf_btn_es")

"""Кнопки конвертации Word в PDF"""
word_button_ru = InlineKeyboardButton("📄Word в PDF", callback_data="word_btn_ru")
word_button_en = InlineKeyboardButton("📄Word to PDF", callback_data="word_btn_en")
word_button_es = InlineKeyboardButton("📄Word a PDF", callback_data="word_btn_es")

"""Кнопки слияния PDF"""
merge_button_ru = InlineKeyboardButton("🔀Слияние PDF", callback_data="merge_btn_ru")
merge_button_en = InlineKeyboardButton("🔀Merge PDF", callback_data="merge_btn_en")
merge_button_es = InlineKeyboardButton("🔀Combinar PDF", callback_data= "merge_btn_es")

"""Кнопки поддержки"""
help_button_ru = InlineKeyboardButton("❓Поддержка", callback_data="help_btn_ru")
help_button_en = InlineKeyboardButton("❓Support", callback_data="help_btn_en")
help_button_es = InlineKeyboardButton("❓Soporte", callback_data="help_btn_es")

"""Кнопки назад"""
back_button_ru = InlineKeyboardButton("🔙Назад", callback_data="back_btn_ru")
back_button_en = InlineKeyboardButton("🔙Back", callback_data="back_btn_en")
back_button_es = InlineKeyboardButton("🔙Atrás", callback_data="back_btn_es")

"""Кнопки настроек"""
settings_button_ru = InlineKeyboardButton("⚙️Настройки", callback_data="set_btn_ru")
settings_button_en = InlineKeyboardButton("⚙️Settings", callback_data="set_btn_en")
settings_button_es = InlineKeyboardButton("⚙️Ajustes", callback_data="set_btn_es")

"""Кнопки смены языка"""
change_lang_button_ru = InlineKeyboardButton("🌐Сменить язык", callback_data="chg_btn_ru")
change_lang_button_en = InlineKeyboardButton("🌐Change language", callback_data="chg_lang_en")
change_lang_button_es = InlineKeyboardButton("🌐Cambiar idioma", callback_data="chg_btn_es")

"""Кнопки выбора языка"""
lang_button_ru = InlineKeyboardButton("🇷🇺Русский", callback_data="lang_btn_ru")
lang_button_en = InlineKeyboardButton("🇬🇧English", callback_data="lang_btn_en")
lang_button_es = InlineKeyboardButton("🇪🇸Español", callback_data="lang_btn_es")
