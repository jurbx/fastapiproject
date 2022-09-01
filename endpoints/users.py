from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.user import User, UserIn, UserUpdate
from .depends import get_user_repository, get_current_user
from repositories.users import UserRepository

router = APIRouter()


@router.get('/', response_model=List[User], response_model_exclude={'hashed_password'})
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0):
    return await users.get_all(limit=limit, skip=skip)


@router.get('/{id}', response_model=User, response_model_exclude={'hashed_password'})
async def read_users(
        id: int,
        users: UserRepository = Depends(get_user_repository),
        ):
    return await users.get_by_id(id=id)


@router.post('/', response_model=User)
async def create(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.patch('/', response_model=User)
async def update_user(
        id: int,
        user: UserUpdate,
        users: UserRepository = Depends(get_user_repository),
        current_user: User = Depends(get_current_user)):
    user_check = await users.get_by_id(id=id)
    if user_check is None or user_check.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found user')
    return await users.update(id=id, u=user)
