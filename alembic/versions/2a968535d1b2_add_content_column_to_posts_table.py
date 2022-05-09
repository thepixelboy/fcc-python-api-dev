"""add content column to posts table

Revision ID: 2a968535d1b2
Revises: 1a7238ca06c3
Create Date: 2022-05-09 15:50:22.136353

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2a968535d1b2"
down_revision = "1a7238ca06c3"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
