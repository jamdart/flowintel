"""empty message

Revision ID: ffffd6a1fa75
Revises: decb78ddf061
Create Date: 2023-11-16 09:34:08.347836

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.exc import OperationalError


# revision identifiers, used by Alembic.
revision = 'ffffd6a1fa75'
down_revision = 'decb78ddf061'
branch_labels = None
depends_on = None

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    try:
        op.create_table('case__galaxy__tags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.Column('case_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('case__galaxy__tags', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_case__galaxy__tags_case_id'), ['case_id'], unique=False)
            batch_op.create_index(batch_op.f('ix_case__galaxy__tags_tag_id'), ['tag_id'], unique=False)
    except OperationalError:
        print("Table 'case__galaxy__tags' already exist")

    try:
        op.create_table('case__template__galaxy__tags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.Column('template_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('case__template__galaxy__tags', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_case__template__galaxy__tags_tag_id'), ['tag_id'], unique=False)
            batch_op.create_index(batch_op.f('ix_case__template__galaxy__tags_template_id'), ['template_id'], unique=False)
    except OperationalError:
        print("Table 'case__template__galaxy__tags' already exist")

    try:
        op.create_table('galaxy',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('version', sa.Integer(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('icon', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('galaxy', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_galaxy_uuid'), ['uuid'], unique=False)
            batch_op.create_index(batch_op.f('ix_galaxy_version'), ['version'], unique=False)
    except OperationalError:
        print("Table 'galaxy' already exist")

    try:
        op.create_table('task__galaxy__tags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.Column('task_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('task__galaxy__tags', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_task__galaxy__tags_tag_id'), ['tag_id'], unique=False)
            batch_op.create_index(batch_op.f('ix_task__galaxy__tags_task_id'), ['task_id'], unique=False)
    except OperationalError:
        print("Table 'task__galaxy__tags' already exist")

    try:
        op.create_table('task__template__galaxy__tags',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('tag_id', sa.Integer(), nullable=True),
        sa.Column('template_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('task__template__galaxy__tags', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_task__template__galaxy__tags_tag_id'), ['tag_id'], unique=False)
            batch_op.create_index(batch_op.f('ix_task__template__galaxy__tags_template_id'), ['template_id'], unique=False)
    except OperationalError:
        print("Table 'task__template__galaxy__tags' already exist")

    try:
        op.create_table('cluster',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('uuid', sa.String(length=36), nullable=True),
        sa.Column('version', sa.Integer(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('meta', sa.String(), nullable=True),
        sa.Column('galaxy_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['galaxy_id'], ['galaxy.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        with op.batch_alter_table('cluster', schema=None) as batch_op:
            batch_op.create_index(batch_op.f('ix_cluster_uuid'), ['uuid'], unique=False)
            batch_op.create_index(batch_op.f('ix_cluster_version'), ['version'], unique=False)
    except OperationalError:
        print("Table 'cluster' already exist")

    try:
        with op.batch_alter_table('tags', schema=None) as batch_op:
            batch_op.add_column(sa.Column('cluster_id', sa.Integer(), nullable=True))
            batch_op.create_foreign_key('fk_tags_cluster_id_cluster', 'cluster', ['cluster_id'], ['id'], ondelete='CASCADE')
    except OperationalError:
        print("Column 'cluster_id' already dropped from 'tags'")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_constraint('fk_tags_cluster_id_cluster', type_='foreignkey')
        batch_op.drop_column('cluster_id')

    with op.batch_alter_table('cluster', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_cluster_version'))
        batch_op.drop_index(batch_op.f('ix_cluster_uuid'))

    op.drop_table('cluster')
    with op.batch_alter_table('task__template__galaxy__tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task__template__galaxy__tags_template_id'))
        batch_op.drop_index(batch_op.f('ix_task__template__galaxy__tags_tag_id'))

    op.drop_table('task__template__galaxy__tags')
    with op.batch_alter_table('task__galaxy__tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_task__galaxy__tags_task_id'))
        batch_op.drop_index(batch_op.f('ix_task__galaxy__tags_tag_id'))

    op.drop_table('task__galaxy__tags')
    with op.batch_alter_table('galaxy', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_galaxy_version'))
        batch_op.drop_index(batch_op.f('ix_galaxy_uuid'))

    op.drop_table('galaxy')
    with op.batch_alter_table('case__template__galaxy__tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_case__template__galaxy__tags_template_id'))
        batch_op.drop_index(batch_op.f('ix_case__template__galaxy__tags_tag_id'))

    op.drop_table('case__template__galaxy__tags')
    with op.batch_alter_table('case__galaxy__tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_case__galaxy__tags_tag_id'))
        batch_op.drop_index(batch_op.f('ix_case__galaxy__tags_case_id'))

    op.drop_table('case__galaxy__tags')
    # ### end Alembic commands ###
