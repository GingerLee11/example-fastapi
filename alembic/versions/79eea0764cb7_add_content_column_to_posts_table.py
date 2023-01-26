"""add content column to posts table

Revision ID: 79eea0764cb7
Revises: c0044f778115
Create Date: 2023-01-25 16:34:08.022395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79eea0764cb7'
down_revision = 'c0044f778115'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column(
        'posts',
        'content'
    )
