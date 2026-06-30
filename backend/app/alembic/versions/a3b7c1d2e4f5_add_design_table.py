"""Add design table

Revision ID: a3b7c1d2e4f5
Revises: fe56fa70289e
Create Date: 2026-06-25 12:00:00.000000

"""
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from alembic import op

# revision identifiers, used by Alembic.
revision = "a3b7c1d2e4f5"
down_revision = "fe56fa70289e"
branch_labels = None
depends_on = None

design_status = sa.Enum(
    "draft",
    "in_review",
    "approved",
    "rejected",
    name="designstatus",
)


def upgrade():
    design_status.create(op.get_bind(), checkfirst=True)
    op.create_table(
        "design",
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
        sa.Column(
            "description", sqlmodel.sql.sqltypes.AutoString(length=4096), nullable=True
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "status",
            design_status,
            nullable=False,
            server_default="draft",
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("owner_id", sa.Uuid(), nullable=False),
        sa.ForeignKeyConstraint(["owner_id"], ["user.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("design")
    design_status.drop(op.get_bind(), checkfirst=True)
