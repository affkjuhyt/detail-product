"""first migrations 3

Revision ID: 99cb62798b44
Revises: acf7a16d2b68
Create Date: 2024-02-28 04:26:23.569637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99cb62798b44'
down_revision: Union[str, None] = 'acf7a16d2b68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
