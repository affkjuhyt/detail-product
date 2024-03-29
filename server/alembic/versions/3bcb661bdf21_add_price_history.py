"""add price history

Revision ID: 3bcb661bdf21
Revises: 2b0abe8ac306
Create Date: 2024-02-28 04:56:23.059844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bcb661bdf21'
down_revision: Union[str, None] = '2b0abe8ac306'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
