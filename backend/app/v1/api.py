# /v1/api.py

# CI/CD autogenned docs deployed on github pages
# https://www.doctave.com/blog/python-export-fastapi-openapi-spec

from fastapi import APIRouter
from .endpoints import update, read_root, query, display, announcements, assignments, uploadfile, files, submit

router = APIRouter()

router.include_router(update.router, tags=["update"], prefix="/update")
router.include_router(read_root.router, tags=["root"], prefix="/read_root")
router.include_router(query.router, tags=["query"], prefix="/query")
router.include_router(display.router, tags=["display"], prefix="/display")
router.include_router(announcements.router, tags=["announcements"], prefix="/announcements")
router.include_router(assignments.router, tags=["assignments"], prefix="/assignments")
router.include_router(uploadfile.router, tags=["uploadfile"], prefix="/uploadfile")
router.include_router(files.router, tags=["files"], prefix="/files")
router.include_router(submit.router, tags=["submit"], prefix="/submit")
