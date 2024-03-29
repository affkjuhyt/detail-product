"""change category parent to nullable

Revision ID: 24df54c8b428
Revises: 777ffdab93cc
Create Date: 2024-02-28 18:23:11.396830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24df54c8b428'
down_revision: Union[str, None] = '777ffdab93cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
