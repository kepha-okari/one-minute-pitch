"""test Pitch without relations

Revision ID: 158e71b17b2d
Revises: 22ea829d25fe
Create Date: 2018-01-03 19:20:22.581851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '158e71b17b2d'
down_revision = '22ea829d25fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    # ### end Alembic commands ###