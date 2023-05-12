"""Add Column  image_url to Pois Table

Revision ID: 4934f7cb180d
Revises: a512a8b276ad
Create Date: 2023-05-11 22:10:22.507780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4934f7cb180d'
down_revision = 'a512a8b276ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('POI', sa.Column('image_url', sa.String(), nullable=True))
    pass


def downgrade():
    op.drop_column('POI', 'image_url')
    pass
