"""empty message

Revision ID: 329acfa205f5
Revises: c0250d59f7ae
Create Date: 2017-11-17 21:29:57.954362

"""

# revision identifiers, used by Alembic.
revision = '329acfa205f5'
down_revision = 'c0250d59f7ae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    op.drop_column('posts', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title', sa.VARCHAR(length=100), nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    # ### end Alembic commands ###