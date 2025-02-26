"""empty message

Revision ID: 7de2327133aa
Revises: e5aaa0e27528
Create Date: 2024-12-03 11:44:36.143494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7de2327133aa'
down_revision = 'e5aaa0e27528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=False))
    op.add_column('messages', sa.Column('username', sa.String(), nullable=False))
    op.drop_column('messages', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('content', sa.VARCHAR(), nullable=False))
    op.drop_column('messages', 'username')
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
