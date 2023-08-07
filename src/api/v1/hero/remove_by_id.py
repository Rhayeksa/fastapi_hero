from fastapi import APIRouter, Path
from sqlalchemy import delete, select

from src.config.database import session
from src.model.hero import Hero
from src.utilities.response import response

router = APIRouter()


@router.delete(
    path="/hero/remove/{id}",
    name="remove by id hero",
    description="remove by id hero",
)
async def remove_by_id(
    id: int = Path()
):
    try:
        query = session.execute(
            select(Hero).
            where(Hero.id == id)
        ).scalars().fetchall()
        if len(query) < 1:
            return await response(code=404, message="ID not found")

        session.execute(
            delete(Hero).
            where(Hero.id == id)
        )

        session.commit()
        return await response(code=200)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
