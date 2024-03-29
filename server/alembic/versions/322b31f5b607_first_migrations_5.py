"""first migrations 5

Revision ID: 322b31f5b607
Revises: c4a585d6b757
Create Date: 2024-02-28 04:28:43.613543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '322b31f5b607'
down_revision: Union[str, None] = 'c4a585d6b757'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
