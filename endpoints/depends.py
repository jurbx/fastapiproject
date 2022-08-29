from starlette import status

from models.user import User
from repositories.jobs import JobsRepository
from repositories.users import UserRepository
from db.base import database
from fastapi import Depends, HTTPException
from core.security import JWTBearer, decode_access_token


def get_user_repository():
    return UserRepository(database)


def get_job_repository():
    return JobsRepository(database)


async def get_current_user(
        users: UserRepository = Depends(get_user_repository),
        token: str = Depends(JWTBearer()),
        ) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Credentials is not valid')
    payload = decode_access_token(token)
    if payload is None:
        raise cred_exception

    email: str = payload.get('sub')
    if email is None:
        raise cred_exception

    user = await users.get_by_email(email=email)
    if user is None:
        raise cred_exception
    return user

