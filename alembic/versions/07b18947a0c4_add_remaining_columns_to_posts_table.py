"""add remaining columns to posts table

Revision ID: 07b18947a0c4
Revises: c46c1c5c7732
Create Date: 2022-05-09 16:16:04.781765

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "07b18947a0c4"
down_revision = "c46c1c5c7732"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column(
            "published", sa.Boolean(), nullable=False, server_default="TRUE"
        ),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
