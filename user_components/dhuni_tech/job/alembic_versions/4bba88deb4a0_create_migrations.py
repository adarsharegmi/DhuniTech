"""create migrations

Revision ID: 4bba88deb4a0
Revises: 837af29ea01d
Create Date: 2022-06-20 23:56:37.915702

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey


# revision identifiers, used by Alembic.
revision = '4bba88deb4a0'
down_revision = '837af29ea01d'
branch_labels = None
depends_on = None


def upgrade():
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
    sa.UniqueConstraint("job_id", "skills_name"),
)



def downgrade():
    pass
