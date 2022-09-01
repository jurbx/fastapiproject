import datetime

from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    hashed_password: str
    is_company: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserIn(BaseModel):
    email: EmailStr
    password: str
    password2: str
    is_company: bool = False

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords don`t match')
        return v


class UserUpdate(BaseModel):
    name: str = ''
    email: EmailStr
    password: str
    password2: str
    is_company: bool = False

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords don`t match')
        return v
