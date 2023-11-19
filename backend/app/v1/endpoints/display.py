# /v1/endpoints/display.py

from fastapi import APIRouter
from typing_extensions import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.v1.functions.canvas_query import get_courses


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def query_courses(token: Annotated[str, Depends(oauth2_scheme)]):
    course_info = get_courses(token)
    return course_info
