from fastapi import APIRouter

from src.api.v1.hero.add import router as add_hero
from src.api.v1.hero.edit_by_id import router as edit_by_id_hero
from src.api.v1.hero.find_all import router as find_all_hero
from src.api.v1.hero.find_by_id import router as find_by_id_hero
from src.api.v1.hero.remove_by_id import router as remove_by_id_hero

router = APIRouter(
    prefix="/v1",
    tags=["V1"]
)

routes = [
    add_hero,
    find_by_id_hero,
    find_all_hero,
    edit_by_id_hero,
    remove_by_id_hero,
]

for route in routes:
    router.include_router(router=route)
