"""create User Table

Revision ID: abd07f48d8a3
Revises: 
Create Date: 2023-03-26 15:29:22.077830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd07f48d8a3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table( 
        "users",
        sa.Column("userId", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("passwordHash", sa.String, nullable=False),
        sa.Column("is_active", sa.Boolean, nullable=False),
        )
    pass


def downgrade():
    op.drop_table("users")
    pass
