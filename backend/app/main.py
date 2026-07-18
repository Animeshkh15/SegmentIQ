from fastapi import FastAPI
from app.api.routes import router as routes_router
from app.api.upload import router as upload_router
from app.api.review import router as review_router
from app.api.results import router as results_router
from app.database.db import Base
from app.database.db import engine
from app.database import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SegmentIQ"
)

app.include_router(routes_router)
app.include_router(upload_router)
app.include_router(review_router)
app.include_router(results_router)