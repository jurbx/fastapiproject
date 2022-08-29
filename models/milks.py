import datetime

from pydantic import BaseModel


class BaseMilks(BaseModel):
    name: str
    rating: int


class Milks(BaseMilks):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class MilksIn(Milks):
    pass
