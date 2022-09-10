"""add_scholarship

Revision ID: 77630bae0439
Revises: be6c5a725ba3
Create Date: 2022-09-09 17:51:45.801824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77630bae0439'
down_revision = 'be6c5a725ba3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school', sa.Column('scholarship', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('school', 'scholarship')
    # ### end Alembic commands ###
