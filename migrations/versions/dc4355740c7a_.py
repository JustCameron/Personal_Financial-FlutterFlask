"""empty message

Revision ID: dc4355740c7a
Revises: b8b4f635084b
Create Date: 2023-07-18 15:13:57.138768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc4355740c7a'
down_revision = 'b8b4f635084b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expense_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('acc_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'account', ['acc_id'], ['id'])

    with op.batch_alter_table('income_channel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('acc_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'account', ['acc_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('income_channel', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('acc_id')

    with op.batch_alter_table('expense_list', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('acc_id')

    # ### end Alembic commands ###