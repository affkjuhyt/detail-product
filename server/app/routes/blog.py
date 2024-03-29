from fastapi import APIRouter, Depends
from app.services import get_all_blog
from app.schema.blog import BlogResponse
from app.dependencies.pgsql import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/list")
async def blogs(db: AsyncSession = Depends(get_db)) -> BlogResponse:
    blogs = await get_all_blog(db)
    return BlogResponse(status="success", data=blogs)
