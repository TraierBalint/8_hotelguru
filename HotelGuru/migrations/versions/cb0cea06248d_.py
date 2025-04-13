"""empty message

Revision ID: cb0cea06248d
Revises: a4fcb54ff2cc
Create Date: 2025-04-13 13:07:33.188346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb0cea06248d'
down_revision = 'a4fcb54ff2cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservations', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.Enum('ACTIVE', 'CANCELLED', 'COMPLETED', name='reservationstatus'),
               existing_nullable=False,
               existing_server_default=sa.text("'ACTIVE'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservations', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.Enum('ACTIVE', 'CANCELLED', 'COMPLETED', name='reservationstatus'),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False,
               existing_server_default=sa.text("'ACTIVE'"))

    # ### end Alembic commands ###
