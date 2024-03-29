"""lazy joinned

Revision ID: 7e1964c8c079
Revises: 41f4dcaecf72
Create Date: 2024-02-28 18:36:51.028723

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e1964c8c079'
down_revision: Union[str, None] = '41f4dcaecf72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
