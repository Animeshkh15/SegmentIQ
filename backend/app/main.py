from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SegmentIQ"
)

app.include_router(router)