from fastapi import FastAPI
from v1.api import router as v1_router

app = FastAPI(description="API for Canvassistant", version="1.0")

# Including API version 1
app.include_router(v1_router, prefix="/v1")
