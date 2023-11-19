# /v1/endpoints/update.py

from fastapi import APIRouter
from typing_extensions import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from v1.functions.canvas_query import get_assignment_info, get_announcements, get_courses
from v1.functions.vectorizeMongo import vectorize_and_store


class Canvas(BaseModel):
    course: int

    
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
    assignment_info = get_assignment_info(token, item.course)
    # return assignment_info

    announcement_info = get_announcements(token, item.course)
#     return announcement_info

    course_info = get_courses(token)
#     return course_info

    # return ping_mongo()

    data_string = str(assignment_info) + str(announcement_info) + str(course_info)

    vectorize_and_store(data_string)

    return {"response": "Data insertion success!"}
