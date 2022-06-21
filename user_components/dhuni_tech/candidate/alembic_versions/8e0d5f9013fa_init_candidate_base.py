"""Init candidate base

Revision ID: 8e0d5f9013fa
Revises: 
Create Date: 2022-06-21 00:01:07.748942

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e0d5f9013fa'
down_revision = None
branch_labels = ('candidate',)
depends_on = None


def upgrade():
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



def downgrade():
    pass
