"""first migrations 6

Revision ID: b4598541ba80
Revises: 322b31f5b607
Create Date: 2024-02-28 04:33:56.388695

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4598541ba80'
down_revision: Union[str, None] = '322b31f5b607'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
