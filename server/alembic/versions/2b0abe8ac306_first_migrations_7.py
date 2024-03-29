"""first migrations 7

Revision ID: 2b0abe8ac306
Revises: b4598541ba80
Create Date: 2024-02-28 04:43:41.794520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b0abe8ac306'
down_revision: Union[str, None] = 'b4598541ba80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
