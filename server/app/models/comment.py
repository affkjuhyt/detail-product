from sqlalchemy import Column, ForeignKey, Integer, String
from app.models.mixins.timestamp_mixin import TimestampMixin
from sqlalchemy.orm import relationship
from app.database import Base


class Comment(TimestampMixin, Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_id = Column(Integer, ForeignKey('items.id'))

    content = Column(String)
    
    user = relationship('User', back_populates='comments')
    item = relationship('Item', back_populates='comments')
    
    parent_id = Column(Integer, ForeignKey('comments.id'))
    replies = relationship('Comment', back_populates='parent', remote_side=[id])
    comment_images = relationship('CommentImage', back_populates='comment')

    parent = relationship('Comment', back_populates='replies')


class CommentImage(TimestampMixin, Base):
    __tablename__ = "comment_images"
    
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comments.id'))
    image_url = Column(String)
    comment = relationship('Comment', back_populates='comment_images')
