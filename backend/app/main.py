# from typing import Union
# from typing_extensions import Annotated
# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel

# from functions.canvas_query import getAssignmentInfo
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# app = FastAPI()


# class Canvas(BaseModel):
#     course: int


# # @app.get("/items/{item_id}")
# # def read_item(item_id: int, q: Union[str, None] = None):
# #     return {"item_id": item_id, "q": q}

# @app.post("/v1/queryCanvas")
# async def query_canvas(item: Canvas, token: Annotated[str, Depends(oauth2_scheme)]):
#     assignment_info = getAssignmentInfo(token, item.course)
#     return assignment_info

# main.py

from fastapi import FastAPI
from v1.api import router as v1_router

app = FastAPI()

# Including API version 1
app.include_router(v1_router, prefix="/v1")
