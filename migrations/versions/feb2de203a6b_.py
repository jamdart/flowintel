"""empty message

Revision ID: feb2de203a6b
Revises: 2418fe20d609
Create Date: 2023-12-01 09:25:52.948536

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError


# revision identifiers, used by Alembic.
revision = 'feb2de203a6b'
down_revision = '2418fe20d609'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.create_table('task__connector',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('task_id', sa.Integer(), nullable=True),
        sa.Column('connector_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('task__connector', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_task__connector_connector_id'), ['connector_id'], unique=False)
            batch_op.create_index(batch_op.f('ix_task__connector_task_id'), ['task_id'], unique=False)
    except OperationalError:
        print("Table 'task__connector' already exist")

    try:
        with op.batch_alter_table('connector', schema=None) as batch_op:
            batch_op.add_column(sa.Column('uuid', sa.String(length=36), nullable=True))
            batch_op.create_index(batch_op.f('ix_connector_uuid'), ['uuid'], unique=False)
    except OperationalError:
        print("Column 'uuid' already in 'connector'")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('connector', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_connector_uuid'))
        batch_op.drop_column('uuid')

    with op.batch_alter_table('task__connector', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task__connector_task_id'))
        batch_op.drop_index(batch_op.f('ix_task__connector_connector_id'))

    op.drop_table('task__connector')
    # ### end Alembic commands ###
