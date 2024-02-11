"""drop user table and update URL table

Revision ID: 311976dfb5d7
Revises: 5264addfa836
Create Date: 2024-02-11 15:49:17.142146

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "311976dfb5d7"
down_revision: Union[str, None] = "5264addfa836"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    def upgrade():
        with op.batch_alter_table("url") as batch_op:
            batch_op.alter_column(
                "url", existing_type=sa.String(), nullable=False, index=False
            )
            batch_op.add_column(
                sa.Column("user_id", sa.Integer(), nullable=True, index=True)
            )

        op.drop_table("user")

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Recreate the User table
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email_address", sa.String(), nullable=False),
        sa.Column("hash_password", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
        sa.UniqueConstraint("email_address"),
    )

    with op.batch_alter_table("url") as batch_op:
        batch_op.alter_column(
            "url", existing_type=sa.String(), nullable=False, index=True
        )
        batch_op.drop_column("user_id")
