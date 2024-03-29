"""add price history 2

Revision ID: 3225c030e740
Revises: f138b82a01d3
Create Date: 2024-02-28 04:57:39.624536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3225c030e740'
down_revision: Union[str, None] = 'f138b82a01d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
