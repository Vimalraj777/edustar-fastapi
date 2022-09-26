"""studentData

Revision ID: 784cdfeb474d
Revises: 
Create Date: 2022-09-26 10:41:26.213261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784cdfeb474d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('studentdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('fname', sa.String(), nullable=False),
    sa.Column('mname', sa.String(), nullable=False),
    sa.Column('phnumber', sa.BigInteger(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    pass


def downgrade() -> None:
    op.drop_table('studentdata')
    pass
