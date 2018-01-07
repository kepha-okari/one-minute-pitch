"""test Pitch without relations

Revision ID: 767eb6847a91
Revises: 369f96ecc53f
Create Date: 2018-01-03 18:55:34.875032

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '767eb6847a91'
down_revision = '369f96ecc53f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_constraint('pitches_category_id_fkey', 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'date_posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.create_foreign_key('pitches_category_id_fkey', 'pitches', 'categories', ['category_id'], ['id'])
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###