"""Add remaining columns to posts table

Revision ID: 004631827859
Revises: 109157c999f7
Create Date: 2023-01-25 16:55:35.061328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004631827859'
down_revision = '109157c999f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column(
            'published', sa.Boolean, nullable=False, server_default='FALSE'
        ),
    )
    op.add_column(
        'posts', 
        sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
        ),
    )


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
