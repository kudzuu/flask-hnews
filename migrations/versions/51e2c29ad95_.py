""" create the Story table

Revision ID: 51e2c29ad95
Revises: 4f2e2c180af
Create Date: 2019-11-11 11:56:01.042947

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '51e2c29ad95'
down_revision = '4f2e2c180af'


def upgrade():
    op.create_table(
        'story',
        sa.Column('title', sa.String(length=300), nullable=False),
        sa.Column('url', sa.Text, nullable=False),
        sa.Column('created_at', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('title', 'url')
    )


def downgrade():
    op.drop_table('story')
