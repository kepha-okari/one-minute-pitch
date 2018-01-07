"""test Pitch without relations

Revision ID: 44477f054b8a
Revises: 767eb6847a91
Create Date: 2018-01-03 19:02:25.641822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44477f054b8a'
down_revision = '767eb6847a91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_pitches_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitches_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitches_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_pitches_id_fkey', 'comments', 'pitches', ['pitches_id'], ['id'])
    # ### end Alembic commands ###