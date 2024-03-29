from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import SessionLocal
from app.dependencies.pgsql import get_db


healthcheck_router = APIRouter()


@healthcheck_router.get("", include_in_schema=False)
@healthcheck_router.get("/", include_in_schema=True)
async def healthcheck(db: AsyncSession = Depends(get_db)):
    query = text("SELECT 1")
    result = await db.execute(query)
    return {"status": "OK", "result": result}
