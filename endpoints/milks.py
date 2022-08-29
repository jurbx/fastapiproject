from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.milks import Milks, BaseMilks
from models.user import User
from .depends import get_milks_repository, get_current_user
from repositories.milks import MilksRepository

router = APIRouter()


@router.get('/', response_model=List[BaseMilks])
async def read_milks(
        milks: MilksRepository = Depends(get_milks_repository())):
    return await milks.get_all()


@router.get('/{id}', response_model=List[BaseMilks])
async def read_milks(
        id: int,
        milks: MilksRepository = Depends(get_milks_repository())):
    return await milks.get_by_id(id=id)


@router.post('/', response_model=List[BaseMilks])
async def read_milks(
        milk: Milks,
        milks: MilksRepository = Depends(get_milks_repository())):
    return await milks.create(m=milk)

