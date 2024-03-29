from typing import List
from sqlalchemy import select
from app.models.blog import Blog


async def get_all_blog(db) -> List[Blog]:
    result = await db.execute(select(Blog))
    return result.scalars().all()
