"""add content column to posts table

Revision ID: df3eb3cad604
Revises: 6280714844af
Create Date: 2022-10-03 20:43:45.760453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df3eb3cad604'
down_revision = '6280714844af'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
