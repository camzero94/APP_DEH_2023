"""create POI, LOI , AOI and SOI tables

Revision ID: a512a8b276ad
Revises: abd07f48d8a3
Create Date: 2023-03-26 17:22:50.166970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a512a8b276ad'
down_revision = 'abd07f48d8a3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "POI",
        sa.Column("poiId", sa.Integer, primary_key=True),
        sa.Column("poiName", sa.String(50), nullable=False),
        sa.Column("poiTitle", sa.String(50)),
        sa.Column("keywords", sa.String(50)),
        sa.Column("period", sa.String(50)),
        sa.Column("year", sa.Integer),
        sa.Column("description", sa.String(150)),
        sa.Column("description_en", sa.String(150)),
        sa.Column("latitude", sa.Float),
        sa.Column("longitude", sa.Float),
        sa.Column("height", sa.Float),
        sa.Column("address", sa.String(50)),
        sa.Column("scope", sa.String(50)),
        sa.Column("source", sa.String),
        sa.Column("creator", sa.String(50)),
        sa.Column("publisher", sa.String(50)),
        sa.Column("contributor", sa.String(50)),
        sa.Column("rights", sa.String(50)),
        sa.Column("verif_open", sa.String(50)),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.userId")),
        )
    op.create_table(
        "SOI",
        sa.Column("soiId", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(50)),
        sa.Column("areaName_en", sa.String(50)),
        sa.Column("uploadTime", sa.DateTime),
        sa.Column("description", sa.String(150)),
        sa.Column("owner", sa.String(50)),
        sa.Column("identifier", sa.String(50)),
        sa.Column("transportation", sa.String(50)),
        sa.Column("open", sa.Boolean),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.userId")),
        sa.Column("poiId", sa.Integer, sa.ForeignKey("POI.poiId")),
        )
    op.create_table(
        "LOI",
        sa.Column("routeId", sa.Integer, primary_key=True),
        sa.Column("routeTitle", sa.String(50)),
        sa.Column("areaName_en", sa.String(50)),
        sa.Column("routeUploadTime", sa.DateTime),
        sa.Column("routeDescription", sa.String(150)),
        sa.Column("routeOwner", sa.String(50)),
        sa.Column("coverage", sa.String(50)),
        sa.Column("duration", sa.String(50)),
        sa.Column("transportation", sa.String(50)),
        sa.Column("open", sa.Boolean),
        sa.Column("poiId", sa.Integer, sa.ForeignKey("POI.poiId")),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.userId")),
        )
    op.create_table(
        "AOI",
        sa.Column("aoiId", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(50)),
        sa.Column("areaName_en", sa.String(50)),
        sa.Column("uploadTime", sa.DateTime),
        sa.Column("description", sa.String(150)),
        sa.Column("owner", sa.String(50)),
        sa.Column("coverage", sa.String(50)),
        sa.Column("numPois", sa.Integer),
        sa.Column("open", sa.Boolean),
        sa.Column("poiId", sa.Integer, sa.ForeignKey("POI.poiId")),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.userId")),
        )
    pass

def downgrade():
    op.drop_table("LOI")
    op.drop_table("AOI")
    op.drop_table("SOI")
    op.drop_table("POI")
    pass
