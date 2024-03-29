"""add provider to item

Revision ID: db588f5f8339
Revises: f4ee62a41601
Create Date: 2024-02-28 15:11:36.563980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db588f5f8339'
down_revision: Union[str, None] = 'f4ee62a41601'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
