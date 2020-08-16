"""add incode and outcode to sale

Revision ID: 3c58af9c8716
Revises: 6305fe90f47c
Create Date: 2020-08-15 09:31:27.012231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c58af9c8716'
down_revision = '6305fe90f47c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sale', sa.Column('incode', sa.String(length=4), nullable=True))
    op.add_column('sale', sa.Column('outcode', sa.String(length=4), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sale', 'outcode')
    op.drop_column('sale', 'incode')
    # ### end Alembic commands ###