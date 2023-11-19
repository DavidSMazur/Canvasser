# /v1/endpoints/update.py

from fastapi import APIRouter
from core.schemas.schema import Canvas
from typing_extensions import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from v1.functions.canvas_query import get_assignment_info, get_announcements, get_courses


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
# async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
#     assignment_info = get_assignment_info(token, item.course)
#     return assignment_info
# async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
#     announcement_info = get_announcements(token, item.course)
#     return announcement_info
async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
    course_info = get_courses(token)
    return course_info
