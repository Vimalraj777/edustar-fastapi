"""auto-vote

Revision ID: 378f4247b663
Revises: 7be75695f562
Create Date: 2022-08-30 18:46:14.190868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '378f4247b663'
down_revision = '7be75695f562'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('posts_id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['posts_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('posts_id', 'users_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    # ### end Alembic commands ###
