from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_button = InlineKeyboardButton('Menu', callback_data='menu')
inline_kb_menu = InlineKeyboardMarkup().add(menu_button)
