import datetime

from pydantic import BaseModel


class BaseProduct(BaseModel):
    title: str
    description: str
    price: int
    is_active: bool
    img: str


class Product(BaseProduct):
    id: int
    user_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ProductIn(BaseProduct):
    pass