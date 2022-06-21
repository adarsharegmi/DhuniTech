"""create migrations

Revision ID: dc06511e8d5a
Revises: 8e0d5f9013fa
Create Date: 2022-06-21 00:01:18.712348

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey

# revision identifiers, used by Alembic.
revision = 'dc06511e8d5a'
down_revision = '8e0d5f9013fa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    "CandidateSkills",
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("candidate_id",
        postgresql.UUID(as_uuid=False),
        ForeignKey("Candidate.id")),
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


def downgrade():
    pass
