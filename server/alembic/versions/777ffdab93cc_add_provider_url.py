"""add provider url

Revision ID: 777ffdab93cc
Revises: 22ab64e57d0e
Create Date: 2024-02-28 18:13:57.563608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '777ffdab93cc'
down_revision: Union[str, None] = '22ab64e57d0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
