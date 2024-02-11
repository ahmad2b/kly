"""Changed user_id type to str

Revision ID: 6cd8937448ad
Revises: 81deef9c2bc1
Create Date: 2024-02-11 21:15:02.077459

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "6cd8937448ad"
down_revision: Union[str, None] = "81deef9c2bc1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("url", "user_id", existing_type=sa.INTEGER(), type_=sa.String())
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("url", "user_id", existing_type=sa.String(), type_=sa.INTEGER())
    # ### end Alembic commands ###
