from typing import Callable

from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.holder import DAO


class DatabaseMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['error', 'update']

    def __init__(self, sessionmaker: Callable[[], AsyncSession]):
        super().__init__()
        self.sessionmaker = sessionmaker

    async def pre_process(self, obj, data, *args):
        session = self.sessionmaker()
        data['session'] = session
        data['dao'] = DAO(session)

    async def post_process(self, obj, data, *args):
        del data['dao']
        session = data.get('session')
        if session:
            await session.close()
            del data['session']
