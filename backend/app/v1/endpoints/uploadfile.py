# /v1/endpoints/uploadfile.py
import shutil

from fastapi import FastAPI, File, UploadFile, APIRouter

app = FastAPI()

router = APIRouter()


@router.post("/")
async def create_upload_file(file: UploadFile):
    name_file = file.filename.replace(" ", "_")
    file_location = f"v1/functions/{name_file}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    return {"file_name": name_file, "file_location": file_location}
