"""empty message

Revision ID: 9512637b5209
Revises: 
Create Date: 2019-04-06 11:39:22.849080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9512637b5209'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=240), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('date', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_date'), 'event', ['date'], unique=True)
    op.create_index(op.f('ix_event_state'), 'event', ['state'], unique=True)
    op.create_index(op.f('ix_event_title'), 'event', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_title'), table_name='event')
    op.drop_index(op.f('ix_event_state'), table_name='event')
    op.drop_index(op.f('ix_event_date'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###
