"""first migrations 4

Revision ID: c4a585d6b757
Revises: 99cb62798b44
Create Date: 2024-02-28 04:27:45.917546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4a585d6b757'
down_revision: Union[str, None] = '99cb62798b44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
