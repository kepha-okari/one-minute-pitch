"""creates pitch and category relationship

Revision ID: 608dc2404de7
Revises: d16ff865fdf9
Create Date: 2018-01-02 19:31:23.691483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '608dc2404de7'
down_revision = 'd16ff865fdf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'category_id')
    # ### end Alembic commands ###
