from aiogram import types, Dispatcher
from aiogram.types import ChatType

from database.api.gateways import Gateway
from keyboard.inline import get_kb_menu


async def start(message: types.Message, gateway: Gateway):
    user = await gateway.user.create(message.chat.id, message.chat.username)
    await message.answer(f'Hello, {user.username if user.username else "human"}')


async def send_menu(message: types.Message, gateway: Gateway):
    user = await gateway.user.get_by_chat_id(message.chat.id)
    await message.answer('Menu:', reply_markup=get_kb_menu(user.username if user.username else 'human'))


def register_menu(dp: Dispatcher):
    dp.register_message_handler(send_menu, commands=['menu'], chat_type=ChatType.PRIVATE)
    dp.register_message_handler(start, commands=['start'], chat_type=ChatType.PRIVATE)
