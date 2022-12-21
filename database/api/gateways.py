import asyncio
import typing

from sqlalchemy import select

from database.models.account import User


class BaseGateway:
    def __init__(self, session):
        self.session = session


class Gateway(BaseGateway):
    """Database gateway"""

    async def merge(self, *args):
        """
        Merge models
        Example: await gateway.merge(User(id=1, username='user1'), User(id=2, username='user2'))
        """
        async with self.session() as s:
            coroutines = []
            for arg in args:
                if arg:
                    coroutines.append(s.merge(arg))
            await asyncio.gather(*coroutines)
            await s.commit()

    async def delete(self, *args):
        """
        Delete models
        Example: await gateway.delete(user1, user2)
        """
        async with self.session() as s:
            coroutines = []
            for arg in args:
                if arg:
                    coroutines.append(s.delete(arg))
            await asyncio.gather(*coroutines)
            await s.commit()

    @property
    def user(self):
        return UserGateway(self.session)


class UserGateway(BaseGateway):
    async def get_by_chat_id(self, chat_id: int) -> User:
        async with self.session() as s:
            user = await s.get(User, chat_id)
        return user

    async def get_all(self) -> typing.Iterable[User]:
        async with self.session() as s:
            users = await s.execute(select(User))
        return users.scalars()

    async def create_new_user(self, chat_id: int, username: str) -> User:
        async with self.session() as s:
            user = await s.merge(User(id=chat_id, username=username))
            await s.commit()
        return user
