"""fix to underscore case

Revision ID: f4ee62a41601
Revises: 3225c030e740
Create Date: 2024-02-28 05:04:50.255911

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4ee62a41601'
down_revision: Union[str, None] = '3225c030e740'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
