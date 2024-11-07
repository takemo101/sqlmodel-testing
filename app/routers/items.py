from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


items_router = APIRouter()


@items_router.get('/items', response_model=list[Item])
async def items() -> list[Item]:
    return [
        Item(
            name='Item1', description='Item1 description', price=9.99, tax=0.99
        ),
        Item(name='Item2', price=19.99),
    ]
