"""empty message

Revision ID: 92aca0edf5eb
Revises: 90c8dd93d179
Create Date: 2023-07-17 16:34:01.379434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92aca0edf5eb'
down_revision = '90c8dd93d179'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income_channel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('monthly_earning', sa.Numeric(precision=10, scale=2), nullable=True))
        batch_op.drop_column('monthlyEarning')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income_channel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('monthlyEarning', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True))
        batch_op.drop_column('monthly_earning')

    # ### end Alembic commands ###
