from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from core.security import verify_password
from models.token import Token, Login
from repositories.users import UserRepository
from .depends import get_user_repository

from core.security import create_access_token

router = APIRouter()


@router.post('/', response_model=Token)
async def login(data: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(data.email)
    if user is None or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    return Token(
        access_token=create_access_token({'sub': user.email}),
        token_type='Bearer'
    )