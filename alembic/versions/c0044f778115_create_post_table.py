"""Create Post table

Revision ID: c0044f778115
Revises: 
Create Date: 2023-01-25 16:26:24.672832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0044f778115'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('posts')
