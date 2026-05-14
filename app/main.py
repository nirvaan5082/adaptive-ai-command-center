from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.db_health import router as db_health_router

app = FastAPI(
    title="Adaptive AI Command Center",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(db_health_router)