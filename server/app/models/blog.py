from sqlalchemy import Column, Integer, String
from app.models.mixins.timestamp_mixin import TimestampMixin
from app.database import Base


class Blog(TimestampMixin, Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    description = Column(String, nullable=False)
    url = Column(String, nullable=True)
