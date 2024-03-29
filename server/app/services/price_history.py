from sqlalchemy import select
from app.models.price_history import PriceHistory
from sqlalchemy.orm.exc import NoResultFound


async def get_price_history_by_item_id(item_id: int, db):
    try:
        price_history = await db.execute(
            select(PriceHistory).filter(PriceHistory.item_id == item_id).order_by(PriceHistory.id.asc())
        )
        price_history = price_history.scalars().all()
        print('price_history: ', price_history)
        return price_history
    except NoResultFound:
        return []


async def get_current_price_by_item_id(item_id: int, db):
    try:
        current_price = await db.execute(
            select(PriceHistory).filter(PriceHistory.item_id == item_id).order_by(PriceHistory.id.desc())
        )
        current_price = current_price.scalars().first()
        return current_price
    except NoResultFound:
        return None
