from datetime import datetime

from fastapi import APIRouter, Body, Path
from sqlalchemy import select, update

from src.config.database import session
from src.model.hero import Hero
from src.utilities.response import response

router = APIRouter()


@router.post(
    path="/hero/edit/{id}",
    name="edit hero by id",
    description="edit hero by id"
)
async def edit_by_id(
    id: int = Path(),
    name: str = Body(""),
    type: str = Body(""),
    description: str = Body(""),
):
    try:
        query = session.execute(
            select(Hero).
            where(Hero.id == id)
        ).scalars().fetchall()
        if len(query) < 1:
            return await response(code=404, message="ID not found")

        if type not in ["", "Knight", "Archer", "Wizard"]:
            return await response(code=400, message="field Type value is not a valid enumeration member; permitted: 'Archer', 'Knight', 'Wizard'")

        query = session.execute(
            select(Hero).
            where(Hero.id == id)
        ).scalars().first()
        name = name if name != "" else query.name  # type: ignore
        type = type if type != "" else query.type  # type: ignore
        description = description if description != "" else query.description  # type: ignore

        session.execute(
            update(Hero).
            where(Hero.id == id).
            values(
                name=name,
                type=type,
                description=description,
                updated_at=datetime.now(),
            )
        )

        session.commit()
        return await response(code=201)
    except Exception as e:
        session.rollback()
        print(f"\n{e}\n")
        return await response(code=500)
    finally:
        session.close()
