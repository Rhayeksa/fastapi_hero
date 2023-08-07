from enum import Enum
from typing import Optional

from fastapi import APIRouter
from sqlalchemy import asc, desc, select

from src.config.database import session
from src.model.hero import Hero
from src.utilities.response import response


class Order(Enum):
    DESC = "DESC"
    ASC = "ASC"


router = APIRouter()


@router.get(
    path="/hero",
    name="find all hero",
    description="find all hero"
)
async def find_all(
    page_size: Optional[int] = None,
    page_num: Optional[int] = None,
    order: Optional[Order] = None,
):
    try:
        page_size = 5 if page_size == None else page_size
        page_num = 1 if page_num == None else page_num
        order = Order.DESC if order == None else order

        data = session.execute(
            select(Hero).
            order_by(desc(Hero.id) if order == Order.DESC else asc(Hero.id)).
            limit(page_size).
            offset((page_num-1) * page_size)
        ).scalars().fetchall()

        return await response(code=200, data=data)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
