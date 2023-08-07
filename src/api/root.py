from fastapi import APIRouter

from src.utilities.response import response

router = APIRouter()


@router.get(
    path="/",
    name="root",
    description="root",
)
async def root():
    return await response(code=200, message="Hello New System")
