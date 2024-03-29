from sqlalchemy.orm import relationship

from app.database import Base

from sqlalchemy import Boolean, Column, Integer, String, Float, ForeignKey

from app.models.mixins.timestamp_mixin import TimestampMixin


class Item(TimestampMixin, Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category", foreign_keys=[category_id], lazy="select")

    images = Column(String, nullable=True, default="[]")
    thumbnail = Column(String, nullable=True)
    
    is_offical_shop = Column(Boolean, default=False)

    historical_sold = Column(Integer, default=0)
    rating_count = Column(Integer, default=0)
    rating_avg = Column(Float, default=0)
    comment_count = Column(Integer, default=0)
    price_before_discount = Column(Float, default=0)

    provider = Column(String, nullable=False)
    provider_url = Column(String, nullable=False)
    
    comments = relationship("Comment", back_populates="item")
