"""create posts table

Revision ID: 13ffb66e6a95
Revises: 
Create Date: 2022-08-30 18:02:51.853139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13ffb66e6a95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('alembic_posts',sa.Column('id',sa.Integer(),nullable=False),
                            sa.Column('title',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('alembic_posts')
    pass
