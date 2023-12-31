"""empty message

Revision ID: 5ff9e22a2f23
Revises: e474d27275ba
Create Date: 2023-07-17 14:55:04.727447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5ff9e22a2f23'
down_revision = 'e474d27275ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('illustrations')
    with op.batch_alter_table('expense_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cost', sa.Numeric(precision=10, scale=2), nullable=True))
        batch_op.add_column(sa.Column('frequency', sa.String(length=255), nullable=True))
        batch_op.drop_column('expense')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('expense_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expense', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True))
        batch_op.drop_column('frequency')
        batch_op.drop_column('cost')

    op.create_table('illustrations',
    sa.Column('iid', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('illustitle', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('piece', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('stage', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('universe', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('illcription', sa.VARCHAR(length=1024), autoincrement=False, nullable=True),
    sa.Column('dateCreated', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('dateCompleted', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('medium', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('genre', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('iid', name='illustrations_pkey')
    )
    # ### end Alembic commands ###
