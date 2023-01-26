from aiogram import Dispatcher

from handlers.menu import register_menu_handlers
from handlers.unknown_messages import register_unknown_messages_handlers


def setup_handlers(dp: Dispatcher):
    register_menu_handlers(dp)
    register_unknown_messages_handlers(dp)
