# /v1/endpoints/announcements.py

from fastapi import APIRouter
from core.schemas.schema import Canvas
from typing_extensions import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from v1.functions.canvas_query import get_announcements


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
    announcement_info = get_announcements(token, item.course)
    return announcement_info
