"""add price_before_discount

Revision ID: eb7bcb5c65d6
Revises: db588f5f8339
Create Date: 2024-02-28 16:08:46.212975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb7bcb5c65d6'
down_revision: Union[str, None] = 'db588f5f8339'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
