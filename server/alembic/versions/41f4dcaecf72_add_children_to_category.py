"""add children to category

Revision ID: 41f4dcaecf72
Revises: 24df54c8b428
Create Date: 2024-02-28 18:32:07.206969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41f4dcaecf72'
down_revision: Union[str, None] = '24df54c8b428'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
