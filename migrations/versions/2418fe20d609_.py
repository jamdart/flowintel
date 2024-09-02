"""empty message

Revision ID: 2418fe20d609
Revises: ab99c63cd1c2
Create Date: 2023-11-29 15:59:18.366612

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError


# revision identifiers, used by Alembic.
revision = '2418fe20d609'
down_revision = 'ab99c63cd1c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.create_table('icon__file',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=64), nullable=True),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('icon__file', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_icon__file_name'), ['name'], unique=True)
            batch_op.create_index(batch_op.f('ix_icon__file_uuid'), ['uuid'], unique=False)
    except OperationalError:
        print("Table 'icon__file' already exist")

    try:
        with op.batch_alter_table('connector__icon', schema=None) as batch_op:
            batch_op.add_column(sa.Column('file_icon_id', sa.Integer(), nullable=True))
            batch_op.create_index(batch_op.f('ix_connector__icon_file_icon_id'), ['file_icon_id'], unique=False)
    except OperationalError:
        print("Column 'file_icon_id' already exist in 'connector__icon'")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('connector__icon', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_connector__icon_file_icon_id'))
        batch_op.drop_column('file_icon_id')

    with op.batch_alter_table('icon__file', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_icon__file_uuid'))
        batch_op.drop_index(batch_op.f('ix_icon__file_name'))

    op.drop_table('icon__file')
    # ### end Alembic commands ###
