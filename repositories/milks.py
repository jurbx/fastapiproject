import datetime

from .base import BaseRepository
from db.milks import milks
from models.milks import Milks, BaseMilks, MilksIn


class MilksRepository(BaseRepository):

    async def get_all(self):
        query = milks.select()
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int):
        query = milks.select().where(milks.c.id == id)
        job = await self.database.fetch_all(query=query)
        if job is None:
            return None
        return BaseMilks.parse_obj(job)

    async def create(self, m: Milks):
        milk = Milks(
            id=0,
            name=m.name,
            rating=m.rating,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**milk.dict()}

        values.pop('id', None)

        query = milks.insert().values(**values)
        milk.id = await self.database.execute(query=query)
        return milk

