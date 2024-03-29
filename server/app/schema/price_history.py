from typing import List
from pydantic import BaseModel
from datetime import date

class PriceHistory(BaseModel):
    price: float
    id: int
    created_at: date
    item_id: int


class PriceHistoryResponse(BaseModel):
    status: str
    data: List[any]
    
    class Config:
        arbitrary_types_allowed=True
