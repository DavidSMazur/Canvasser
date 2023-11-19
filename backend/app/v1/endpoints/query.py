# /v1/endpoints/query.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def query():
    return "Query hit"


# @router.post("/", response_model=ItemSchema)
# async def create_item(item: ItemSchema):
#     return item
