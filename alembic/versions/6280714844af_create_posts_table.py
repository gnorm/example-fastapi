"""create posts table

Revision ID: 6280714844af
Revises: 
Create Date: 2022-10-03 20:38:48.401233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6280714844af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('video_time', sa.String(), nullable=False, server_default=sa.text("'-'"))
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
