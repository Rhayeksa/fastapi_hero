from datetime import datetime

from fastapi import APIRouter, Body
from sqlalchemy import insert, select

from src.config.database import session
from src.model.hero import Hero
from src.utilities.response import response

router = APIRouter()


@router.post(
    path="/hero/add",
    name="add hero",
    description="add hero"
)
async def add(
    name: str = Body(""),
    type: str = Body("Archer"),
    description: str = Body(""),
):
    try:
        query = session.execute(
            select(Hero).
            where(Hero.name == name)
        ).scalars().fetchall()
        if len(query) > 0:
            return await response(code=409, message="Name already exist")

        if "" in [name, type, description]:
            return await response(code=400, message="Name, type and description is required")

        if type not in ["Knight", "Archer", "Wizard"]:
            return await response(code=400, message="field Type value is not a valid enumeration member; permitted: 'Archer', 'Knight', 'Wizard'")

        session.execute(
            insert(Hero).
            values(
                name=name,
                type=type,
                description=description,
                created_at=datetime.now(),
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
