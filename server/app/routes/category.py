from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.services import get_categories
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies.pgsql import get_db

router = APIRouter()


@router.get("/list")
async def categories(db: AsyncSession = Depends(get_db)):
    categories = await get_categories(db)
    formatted_categories = await convert_catefories(categories)

    return JSONResponse(content={"status": "success", "data": {"categories": formatted_categories}})


async def convert_catefories(categories):
    formatted_categories = []
    for category in categories:
        formatted_children = []
        if category.children:
            for child in category.children:
                formatted_children.append({
                    "id": child.id,
                    "slug": child.slug,
                    "name": child.name,
                    "url_thumbnail": child.url_thumbnail,
                    "level": child.level,
                    "parent_id": child.parent_id,
                    "relative_path": child.relative_path
                })
        formatted_categories.append({
            "id": category.id,
            "slug": category.slug,
            "name": category.name,
            "url_thumbnail": category.url_thumbnail,
            "level": category.level,
            "parent_id": category.parent_id,
            "relative_path": category.relative_path,
            "childs": formatted_children
        })
    
    return formatted_categories
