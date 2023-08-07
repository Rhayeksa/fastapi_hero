from fastapi import APIRouter, Path
from sqlalchemy import select

from src.config.database import session
from src.model.hero import Hero
from src.utilities.response import response

router = APIRouter()


@router.get(
    path="/hero/{id}",
    name="find by id hero",
    description="find by id hero"
)
async def find_by_id(
    id: int = Path(),
):
    try:
        data = session.execute(
            select(Hero).
            where(Hero.id == id)
        ).scalars().fetchall()
        if len(data) < 1:
            return await response(code=404, message="ID not found")

        return await response(code=200, data=data[0])
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
