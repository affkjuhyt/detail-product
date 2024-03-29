"""add relational category

Revision ID: 22ab64e57d0e
Revises: eb7bcb5c65d6
Create Date: 2024-02-28 16:34:10.699241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22ab64e57d0e'
down_revision: Union[str, None] = 'eb7bcb5c65d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
