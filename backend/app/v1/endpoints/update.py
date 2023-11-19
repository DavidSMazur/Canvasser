# /v1/endpoints/update.py

from fastapi import APIRouter
# from core.schemas.schema import ItemSchema

router = APIRouter()

@router.get("/")
async def update():
    return "Hi"


# @router.post("/", response_model=ItemSchema)
# async def create_item(item: ItemSchema):
#     return item
