"""empty message

Revision ID: 63bf35428bef
Revises: b541e69683c7
Create Date: 2020-07-08 10:09:09.993896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63bf35428bef'
down_revision = 'b541e69683c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('_password', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', '_password')
    # ### end Alembic commands ###
