from typing import List, Optional
from pydantic import BaseModel

class CategoryData(BaseModel):
    id: int
    slug: str
    name: str
    url_thumbnail: str
    level: int
    parent_id: int
    relative_path: int
    childs: Optional[List['CategoryData']]


class Category(BaseModel):
    categories: List[CategoryData]


class CategoryResponse(BaseModel):
    status: str
    data: Category
