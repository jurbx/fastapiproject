from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.products import Product, BaseProduct, ProductIn
from models.user import User
from .depends import get_job_repository, get_current_user
from repositories.products import ProductsRepository

router = APIRouter()


@router.get('/', response_model=List[Product])
async def read_products(
        products: ProductsRepository = Depends(get_job_repository),
        limit: int = 100,
        skip: int = 0):
    return await products.get_all(limit=limit, skip=skip)


@router.get('/{user_id}', response_model=List[Product])
async def read_user_products(
        user_id: int,
        products: ProductsRepository = Depends(get_job_repository)):
    return await products.get_by_user(user_id)
# current_user: User = Depends(get_current_user)


@router.get('/{id}', response_model=Product)
async def read_product(
        id: int,
        products: ProductsRepository = Depends(get_job_repository),
        ):
    return await products.get_by_id(id=id)


@router.post('/', response_model=Product)
async def create(
        product: ProductIn,
        products: ProductsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    return await products.create(user_id=int(current_user.id), p=product)


@router.patch('/', response_model=Product)
async def update_product(
        id: int,
        product: ProductIn,
        products: ProductsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    product_check = await products.get_by_id(id=id)
    if product_check.user_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found user')
    if product_check is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found product')
    return await products.update(user_id=int(current_user.id), id=id, p=product)


@router.delete('/')
async def delete_product(
        id: int,
        products: ProductsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    product = await products.get_by_id(id=id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found')
    if product.user_id != int(current_user.id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Current user has no access')

    result = await products.delete(id=id)

    return {'status': True}