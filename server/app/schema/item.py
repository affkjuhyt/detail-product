from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from app.schema.category import CategoryData

class Item(BaseModel):
    slug: str
    name: str
    category_id: int
    thumbnail: str
    rating_count: int
    comment_count: int
    provider: str
    provider_url: str
    created_at: date
    description: str
    id: int
    images: List[str]
    historical_sold: int
    rating_avg: float
    price_before_discount: float
    category: CategoryData
    # categories: List[CategoryData]
    current_price: float
    
    class Config:
        arbitrary_types_allowed = True


class PriceInsight(BaseModel):        
    product_base_id: int
    classify_price: str
    current_price: float
    ratio: float
    min_price: float
    max_price: float
    avg_price: float
    delta_price: Optional[None]


class ItemResult(BaseModel):
    product_base_id: int
    name: str
    price: float
    price_before_discount: float
    url_thumbnail: str
    is_offical_shop: Optional[bool]
    rating_count: int
    rating_avg: float
    historical_sold: int
    price_insight: PriceInsight
        

class ItemRecent(BaseModel):
    products: List[ItemResult]


class ItemDetail(BaseModel):
    item: Item


class ItemDetailResponse(BaseModel):
    status: str
    data: ItemDetail
    

class ItemRecentResponse(BaseModel):
    status: str
    data: ItemRecent
