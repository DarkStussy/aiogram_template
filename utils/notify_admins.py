import logging
import typing

from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound


async def notify_admins(dp: Dispatcher, admins: typing.Sequence[int]):
    for admin_id in admins:
        try:
            await dp.bot.send_message(chat_id=admin_id, text='Bot started!')
        except ChatNotFound:
            pass
        except Exception as e:
            logging.exception(e)
