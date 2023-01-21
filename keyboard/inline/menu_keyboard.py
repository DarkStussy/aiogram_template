from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_kb_menu(username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup().add(InlineKeyboardButton(f'Button for {username}', callback_data='button_menu'))
