# /v1/api.py

from fastapi import APIRouter
from .endpoints import update, read_root

router = APIRouter()

router.include_router(update.router, tags=["update"], prefix="/update")
router.include_router(read_root.router, tags=["root"], prefix="/read_root")
