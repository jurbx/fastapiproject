import datetime

from .base import BaseRepository
from db.jobs import jobs
from models.jobs import BaseJob, Job, JobIn


class JobsRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0):
        query = jobs.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int):
        query = jobs.select().where(jobs.c.id == id)
        job = await self.database.fetch_one(query=query)
        if job is None:
            return None
        return BaseJob.parse_obj(job)

    async def create(self, user_id: int, j: JobIn):
        job = Job(
            id=0,
            user_id=user_id,
            title=j.title,
            description=j.description,
            salary_from=j.salary_from,
            salary_to=j.salary_to,
            is_active = j.is_active,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**job.dict()}
        values.pop('id', None)

        query = jobs.insert().values(**values)
        job.id = await self.database.execute(query=query)
        return job

    async def update(self, id: int, user_id: int, j: JobIn):
        job = Job(
            id=id,
            user_id=user_id,
            title=j.title,
            description=j.description,
            salary_from=j.salary_from,
            salary_to=j.salary_to,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**job.dict()}
        values.pop('created_at', None)
        values.pop('id', None)

        query = jobs.update().where(jobs.c.id==id).values(**values)
        await self.database.execute(query)
        return job

    async def get_by_email(self, email: str):
        query = jobs.select().where(jobs.c.email == email)
        job = await self.database.fetch_one(query=query)
        if job is None:
            return None
        return BaseJob.parse_obj(job)