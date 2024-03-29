"""add price history 1

Revision ID: f138b82a01d3
Revises: 3bcb661bdf21
Create Date: 2024-02-28 04:56:49.047010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f138b82a01d3'
down_revision: Union[str, None] = '3bcb661bdf21'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
