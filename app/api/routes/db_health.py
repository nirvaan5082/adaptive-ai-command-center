from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine

router = APIRouter(
    prefix="/db-health",
    tags=["Database"]
)

@router.get("/")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "connected"
        }

    except Exception as error:
        return {
            "database": "failed",
            "error": str(error)
        }
    