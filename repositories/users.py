import datetime

from core.security import hash_password
from .base import BaseRepository
from db.users import users
from typing import List
from models.user import User, UserIn


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0):
        query = users.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query, )

    async def get_by_id(self, id: int):
        query = users.select().where(users.c.id == id)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)

    async def create(self, u: UserIn):
        user = User(
            id=0,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop('id', None)

        query = users.insert().values(**values)
        user.id = await self.database.execute(query)
        return user

    async def update(self, id: int, u: UserIn):
        user = User(
            id=id,
            name=u.name,
            email=u.email,
            hashed_password=hash_password(u.password),
            is_company=u.is_company,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop('created_at', None)
        values.pop('id', None)

        query = users.update().where(users.c.id==id).values(**values)
        await self.database.execute(query)
        return user

    async def get_by_email(self, email: str):
        query = users.select().where(users.c.email == email)
        user = await self.database.fetch_one(query=query)
        if user is None:
            return None
        return User.parse_obj(user)