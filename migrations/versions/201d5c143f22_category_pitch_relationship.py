"""category pitch relationship

Revision ID: 201d5c143f22
Revises: 5dd5ba8f7aaa
Create Date: 2018-01-12 14:29:01.557526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '201d5c143f22'
down_revision = '5dd5ba8f7aaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vote', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitches_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'pitches', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_table('votes')
    # ### end Alembic commands ###
