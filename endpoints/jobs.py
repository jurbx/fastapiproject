from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.jobs import Job, BaseJob
from models.user import User
from .depends import get_job_repository, get_current_user
from repositories.jobs import JobsRepository

router = APIRouter()


@router.get('/', response_model=List[BaseJob], response_model_exclude={'hashed_password'})
async def read_jobs(
        jobs: JobsRepository = Depends(get_job_repository),
        limit: int = 100,
        skip: int = 0):
    return await jobs.get_all(limit=limit, skip=skip)


@router.get('/{id}', response_model=BaseJob, response_model_exclude={'hashed_password'})
async def read_jobs(
        id: int,
        jobs: JobsRepository = Depends(get_job_repository),
        ):
    return await jobs.get_by_id(id=id)


@router.post('/', response_model=BaseJob)
async def create(
        job: Job,
        jobs: JobsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    return await jobs.create(user_id=current_user.id, j=job)


@router.patch('/', response_model=BaseJob)
async def update_job(
        id: int,
        job: Job,
        jobs: JobsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    job_check = await jobs.get_by_id(id=id)
    if job_check is None or job_check.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found user')
    return await jobs.update(id=id, j=job)
