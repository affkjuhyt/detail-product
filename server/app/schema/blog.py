from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    id: int
    title: str
    image_url: str
    description: str
    url: str
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class BlogResponse(BaseModel):
    status: str
    data: List[Blog]
