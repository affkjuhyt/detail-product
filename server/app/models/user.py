from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.mixins.timestamp_mixin import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    url_image = Column(String, nullable=True)
    
    comments = relationship("Comment", back_populates="user")
