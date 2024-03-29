from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload

from app.database import SessionLocal
from app.models.category import Category
from sqlalchemy.orm.exc import NoResultFound


async def get_category_by_id(category_id: int, db):
    try:
        result = await db.execute(
            select(Category).filter(Category.id == category_id).options(joinedload(Category.children))
        )
        category = result.scalars().unique().one()
        
        print('category is: ', category)
        return category
    except NoResultFound:
        return None

async def recursive_parent_category(category_id: int, db):
    parent_categories = []
    while category_id != 0:
        print('start get category id: ', category_id)
        category = await get_category_by_id(category_id, db)

        if category is not None:
            parent_categories.append(category)
            category_id = category.parent_id
        else:
            category_id = 0
    return parent_categories


async def get_categories(db):
    result = await db.execute(select(Category).filter(Category.parent_id == None).options(selectinload(Category.children)))
    return result.scalars().all()
