from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.products import Product, BaseProduct
from models.user import User
from .depends import get_job_repository, get_current_user
from repositories.products import ProductsRepository

router = APIRouter()


@router.get('/', response_model=List[BaseProduct], response_model_exclude={'hashed_password'})
async def read_products(
        products: ProductsRepository = Depends(get_job_repository),
        limit: int = 100,
        skip: int = 0):
    return await products.get_all(limit=limit, skip=skip)


@router.get('/{id}', response_model=BaseProduct, response_model_exclude={'hashed_password'})
async def read_product(
        id: int,
        products: ProductsRepository = Depends(get_job_repository),
        ):
    return await products.get_by_id(id=id)


@router.post('/', response_model=BaseProduct)
async def create(
        product: Product,
        products: ProductsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    return await products.create(user_id=current_user.id, p=product)


@router.patch('/', response_model=BaseProduct)
async def update_product(
        id: int,
        job: Product,
        jobs: ProductsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    job_check = await jobs.get_by_id(id=id)
    if job_check is None or job_check.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found user')
    return await jobs.update(id=id, p=job)


@router.delete('/')
async def delete_products(
        id: int,
        products: ProductsRepository = Depends(get_job_repository),
        current_user: User = Depends(get_current_user)):
    product = await products.get_by_id(id=id)
    not_found = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Job not found')
    if product is None or product.user_id != current_user.id:
        raise not_found

    result = await products.delete(id=id)

    if result is None:
        raise not_found

    return {'status': True}