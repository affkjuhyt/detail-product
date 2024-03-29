from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from app.services.item import get_item_detail, get_recent_item
from app.services.price_history import get_price_history_by_item_id
from app.schema.price_history import PriceHistoryResponse
from app.schema.item import ItemRecentResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies.pgsql import get_db

router = APIRouter()


@router.get("/{item_id}/detail")
async def read_item_detail(item_id: int, db: AsyncSession = Depends(get_db)):
    item_detail = await get_item_detail(item_id, db)
    
    item_detail["updated_at"] = item_detail["updated_at"].isoformat()
    item_detail["created_at"] = item_detail["created_at"].isoformat()
    item_detail["category"] = await item_detail["category"].to_dict()
    item_detail["categories"] = [await category.to_dict() for category in item_detail["categories"]]
    
    return JSONResponse(content={"status": "success", "data": {"item": item_detail}})


@router.get("/{item_id}/price-history")
async def read_item_price_history(item_id: int, db: AsyncSession = Depends(get_db)):
    price_history = await get_price_history_by_item_id(item_id, db)
    
    print('price_history: ', price_history)
    
    return {
        "status": "success",
        "data": price_history
    }
    

@router.get("/recent")
async def get_recent_items(limit: int = Query(20), t: int = Query(None, description="Timestamp"), db: AsyncSession = Depends(get_db)):
    products = await get_recent_item(limit=limit, t=t, db=db)

    return ItemRecentResponse(status="success", data={"products": products})
