"""for skill job

Revision ID: 05608fca53a3
Revises: ee5b28c500c0
Create Date: 2022-06-20 22:51:33.060005

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey

# revision identifiers, used by Alembic.
revision = '05608fca53a3'
down_revision = 'ee5b28c500c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
    "JobSkills",
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("job_id",
        postgresql.UUID(as_uuid=False),
        ForeignKey("Job.id")),
    sa.Column("skills_name", sa.String(255)),
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
