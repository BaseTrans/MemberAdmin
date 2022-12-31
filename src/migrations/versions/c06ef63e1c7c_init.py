"""init

Revision ID: c06ef63e1c7c
Revises: 
Create Date: 2023-01-20 17:14:16.637271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c06ef63e1c7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('door_id', sa.Integer(), nullable=True),
    sa.Column('cabinet_num', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('charge_amount_per_month', sa.Float(), nullable=True),
    sa.Column('last_pay_date', sa.DateTime(), nullable=True),
    sa.Column('last_pay_amount', sa.Float(), nullable=True),
    sa.Column('next_pay_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('BankRecords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaction_date', sa.DateTime(), nullable=False),
    sa.Column('account_date', sa.DateTime(), nullable=False),
    sa.Column('summary', sa.String(), nullable=True),
    sa.Column('transaction_amount', sa.Numeric(), nullable=False),
    sa.Column('balance', sa.Numeric(), nullable=False),
    sa.Column('remark', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PaymentRecords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transaction_id', sa.String(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['Account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PaymentRecords')
    op.drop_table('BankRecords')
    op.drop_table('Account')
    # ### end Alembic commands ###
