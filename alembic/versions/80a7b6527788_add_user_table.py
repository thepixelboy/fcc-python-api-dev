"""add user table

Revision ID: 80a7b6527788
Revises: 2a968535d1b2
Create Date: 2022-05-09 15:56:23.313340

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "80a7b6527788"
down_revision = "2a968535d1b2"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
