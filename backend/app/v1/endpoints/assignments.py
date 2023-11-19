# /v1/endpoints/assignments.py

from fastapi import APIRouter
from core.schemas.schema import Canvas
from typing_extensions import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from v1.functions.canvas_query import get_assignment_info


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
    assignment_info = get_assignment_info(token, item.course)
    return assignment_info
