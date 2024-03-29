from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import relationship

from app.database import Base, SessionLocal
from app.models.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy.orm import joinedload


class Category(TimestampMixin, Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, index=True)
    name = Column(String, nullable=False)
    url_thumbnail = Column(String, nullable=False)
    level = Column(Integer, default=0)
    parent_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    relative_path = Column(String, nullable=True)

    children = relationship("Category", foreign_keys=[parent_id], lazy="joined")
    
    async def to_dict(self, session=None):
        if not session:
            session = SessionLocal()

        async with session.begin():
            result = await session.execute(
                select(Category).filter(Category.id == self.id).options(joinedload(Category.children))
            )
            category_with_children = result.unique().scalar()

        return {
            "id": category_with_children.id,
            "slug": category_with_children.slug,
            "name": category_with_children.name,
            "url_thumbnail": category_with_children.url_thumbnail,
            "level": category_with_children.level,
            "parent_id": category_with_children.parent_id,
            "relative_path": category_with_children.relative_path,
            "childs": [await child.to_dict(session=session) for child in category_with_children.children]
                if category_with_children.children else []
        }
