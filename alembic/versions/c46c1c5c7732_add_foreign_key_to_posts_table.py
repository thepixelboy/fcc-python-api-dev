"""add foreign-key to posts table

Revision ID: c46c1c5c7732
Revises: 80a7b6527788
Create Date: 2022-05-09 16:05:09.431803

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c46c1c5c7732"
down_revision = "80a7b6527788"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
