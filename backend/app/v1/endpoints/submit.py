# /v1/endpoints/update.py

from fastapi import APIRouter
from core.schemas.schema import Submit
from typing_extensions import Annotated
from fastapi import Depends, UploadFile
from fastapi.security import OAuth2PasswordBearer

from v1.functions.canvas_submission import submit_file


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/")
async def submission(course: Submit, token: Annotated[str, Depends(oauth2_scheme)]):
    file_response = submit_file(token, course.file_path, course.course_id, course.assignment_id)
    return file_response