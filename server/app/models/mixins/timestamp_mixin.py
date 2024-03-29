from sqlalchemy import Column, DateTime, func, TIMESTAMP
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(
            TIMESTAMP,
            server_default=func.now(),
            nullable=False,
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            TIMESTAMP,
            server_default=func.now(),
            onupdate=func.current_timestamp(),
            nullable=False,
        )
