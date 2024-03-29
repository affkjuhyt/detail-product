"""first migrations 1

Revision ID: 641e4a413f8d
Revises: d42ac8c0f3b1
Create Date: 2024-02-28 04:25:21.756990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '641e4a413f8d'
down_revision: Union[str, None] = 'd42ac8c0f3b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
