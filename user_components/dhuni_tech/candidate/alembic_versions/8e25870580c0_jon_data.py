"""jon data

Revision ID: 8e25870580c0
Revises: 
Create Date: 2022-06-20 22:47:26.270437

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e25870580c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    "Candidate",
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("first_name", sa.String(255)),
    sa.Column("last_name", sa.String(255)),
    sa.Column("status", sa.String(255)),
    sa.Column(
        "created_at",
        sa.TIMESTAMP(timezone=True),
        default=sa.func.now(),
    ),
    sa.Column(
        "updated_at",
        sa.TIMESTAMP(timezone=True),
        default=sa.func.now(),
        onupdate=sa.func.now(),
    ),
)


def downgrade() -> None:
    pass
