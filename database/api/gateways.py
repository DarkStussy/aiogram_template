from database.models.account import User


class BaseGateway:
    def __init__(self, session):
        self.session = session


class Gateway(BaseGateway):
    """Database gateway"""

    @property
    def user(self):
        return UserGateway(self.session)


class UserGateway(BaseGateway):
    async def get_by_chat_id(self, chat_id: int) -> User:
        async with self.session() as s:
            user = await s.get(User, chat_id)
        return user

    async def create_new_user(self, chat_id: int, username: str) -> User:
        async with self.session() as s:
            user = await s.merge(User(id=chat_id, username=username))
            await s.commit()
        return user
