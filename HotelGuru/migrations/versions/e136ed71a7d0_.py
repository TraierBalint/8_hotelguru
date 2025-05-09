"""empty message

Revision ID: e136ed71a7d0
Revises: 
Create Date: 2025-04-17 17:00:09.339185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e136ed71a7d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('type', sa.Enum('SINGLE', 'DOUBLE', 'SUITE', name='roomtype'), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('AVAILABLE', 'RESERVED', 'MAINTENANCE', name='roomstatus'), nullable=False),
    sa.Column('deleted', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=30), nullable=False),
    sa.Column('street', sa.String(length=30), nullable=False),
    sa.Column('postalcode', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('check_in', sa.Date(), nullable=False),
    sa.Column('check_out', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('ACTIVE', 'CANCELLED', 'COMPLETED', name='reservationstatus'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userroles',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='fk_userroles_role_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_userroles_user_id')
    )
    op.create_table('extraservices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('reservation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['reservation_id'], ['reservations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reservation_id', sa.Integer(), nullable=False),
    sa.Column('total_amount', sa.Float(), nullable=False),
    sa.Column('issued_at', sa.Date(), nullable=False),
    sa.Column('paid', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['reservation_id'], ['reservations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation_rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reservation_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['reservation_id'], ['reservations.id'], name='fk_reservationroom_reservation_id', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['room_id'], ['Rooms.id'], name='fk_reservationroom_room_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invoice_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.String(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice_items')
    op.drop_table('reservation_rooms')
    op.drop_table('invoices')
    op.drop_table('extraservices')
    op.drop_table('userroles')
    op.drop_table('reservations')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('addresses')
    op.drop_table('Rooms')
    # ### end Alembic commands ###
