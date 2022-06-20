"""for skill

Revision ID: ee5b28c500c0
Revises: 
Create Date: 2022-06-20 22:51:28.308437

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = 'ee5b28c500c0'
down_revision = '8e25870580c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
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


def downgrade() -> None:
    pass
