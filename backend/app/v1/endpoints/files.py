# /v1/endpoints/files.py

from typing import Annotated

from fastapi import FastAPI, File, UploadFile, APIRouter

app = FastAPI()

router = APIRouter()


@router.post("/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}
