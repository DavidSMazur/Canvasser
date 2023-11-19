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
async def query_canvas(item: Submit, file: UploadFile, token: Annotated[str, Depends(oauth2_scheme)]):
    file_response = submit_file(token, file, course_id, assignment_id)
    return file_response