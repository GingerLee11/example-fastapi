"""Add foreign key to posts table

Revision ID: 109157c999f7
Revises: 6bb6ac32a3a8
Create Date: 2023-01-25 16:51:04.474805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '109157c999f7'
down_revision = '6bb6ac32a3a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False),
    )
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
