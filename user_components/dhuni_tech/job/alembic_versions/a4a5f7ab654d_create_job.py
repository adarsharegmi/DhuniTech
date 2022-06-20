"""create_job

Revision ID: a4a5f7ab654d
Revises: 
Create Date: 2022-06-20 22:48:35.960008

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'a4a5f7ab654d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    "Job",
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("job_title", sa.String(255)),
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
