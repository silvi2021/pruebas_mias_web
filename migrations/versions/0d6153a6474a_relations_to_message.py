"""relations to message

Revision ID: 0d6153a6474a
Revises: 814bcc596624
Create Date: 2022-12-07 21:52:00.654623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d6153a6474a'
down_revision = '814bcc596624'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###