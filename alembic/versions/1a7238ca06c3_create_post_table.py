"""create post table

Revision ID: 1a7238ca06c3
Revises: 
Create Date: 2022-05-09 15:35:15.521264

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1a7238ca06c3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
