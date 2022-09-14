import datetime

from .base import BaseRepository
from db.products import products
from models.products import BaseProduct, Product, ProductIn


class ProductsRepository(BaseRepository):

    async def get_all(self, limit: int = 100, skip: int = 0):
        query = products.select().limit(limit).offset(skip)
        return await self.database.fetch_all(query=query)

    async def get_by_id(self, id: int):
        query = products.select().where(products.c.id == id)
        product = await self.database.fetch_one(query=query)
        if product is None:
            return None
        return BaseProduct.parse_obj(product)

    async def delete(self, id:int):
        query = products.delete().where(products.c.id == id)
        return await self.database.execute(query=query)

    async def create(self, user_id: int, p: ProductIn):
        product = Product(
            id=0,
            user_id=user_id,
            title=p.title,
            description=p.description,
            price=p.price,
            img=p.img,
            is_active = p.is_active,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**product.dict()}
        values.pop('id', None)

        query = products.insert().values(**values)
        product.id = await self.database.execute(query=query)
        return product

    async def update(self, id: int, user_id: int, p: ProductIn):
        product = Product(
            id=id,
            user_id=user_id,
            title=p.title,
            description=p.description,
            price=p.price,
            img=p.img,
            created_at=datetime.datetime.utcnow(),
            updated_at=datetime.datetime.utcnow(),
        )

        values = {**product.dict()}
        values.pop('created_at', None)
        values.pop('id', None)

        query = products.update().where(products.c.id == id).values(**values)
        await self.database.execute(query)
        return product

    async def get_by_email(self, email: str):
        query = products.select().where(products.c.email == email)
        product = await self.database.fetch_one(query=query)
        if product is None:
            return None
        return BaseProduct.parse_obj(product)