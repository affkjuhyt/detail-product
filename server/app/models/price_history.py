from sqlalchemy import Column, TIMESTAMP, func, Double, Integer, ForeignKey

from app.database import Base


class PriceHistory(Base):
    __tablename__ = 'price_histories'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    price = Column(Double)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=func.now())
