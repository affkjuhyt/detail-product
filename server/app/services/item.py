from datetime import datetime
import json

from fastapi import HTTPException, status
from sqlalchemy import desc, select
from app.services.category import recursive_parent_category
from app.services.price_history import get_current_price_by_item_id
from app.models.item import Item

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import selectinload

from app.database import SessionLocal


async def get_item_by_id(item_id: int, db):
    try:
        result = await db.execute(
            select(Item).options(selectinload(Item.category)).filter(Item.id == item_id)
        )
        item = result.scalars().one()
        return item
    except NoResultFound:
        return None


async def get_item_detail(item_id: int, db):
    item = await get_item_by_id(item_id, db)
    
    print('items: ', item)

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Item {item_id} not found')

    print('item category: ', item.category_id)
    categories = await recursive_parent_category(item.category_id, db)

    item_dict = item.__dict__
    print('item dict is: ', item_dict)
    item_copy = {key: item_dict[key] for key in item_dict if not key.startswith('_')}

    item_copy["categories"] = categories

    item_copy["images"] = json.loads(item.images)

    current_price = await get_current_price_by_item_id(item_id, db)
    item_copy["current_price"] = current_price.price

    return item_copy


async def get_recent_item(limit, t, db):
    if t is None:
        timestamp = datetime.now()
    else:
        timestamp = datetime.fromtimestamp(t)
    
    recent_items = await db.execute(
        select(Item)
        .filter(Item.created_at <= timestamp)
        .order_by(desc(Item.created_at))
        .limit(limit)
    )
    
    products = []
    for item in recent_items.scalars().all():
        current_price = await get_current_price_by_item_id(item.id, db)
        
        product_info = {
            "product_base_id": item.id,
            "name": item.name,
            "price": current_price.price,
            "price_before_discount": item.price_before_discount,
            "url_thumbnail": item.thumbnail,
            "is_offical_shop": item.is_offical_shop,
            "rating_count": item.rating_count,
            "rating_avg": item.rating_avg,
            "historical_sold": item.historical_sold,
            "price_insight": { # I think value get from model ML
                "product_base_id": item.id,
                "classify_price": "bad",
                "current_price": current_price.price,
                "ratio": 1.0, 
                "min_price": current_price.price,
                "max_price": item.price_before_discount,
                "avg_price": (current_price.price + item.price_before_discount) / 2,
                "delta_price": None
            }
        }
        products.append(product_info)
        
        return products
