"""Init Job skills

Revision ID: 837af29ea01d
Revises: 
Create Date: 2022-06-20 23:55:27.307697

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '837af29ea01d'
down_revision = None
branch_labels = ('job',)
depends_on = None


def upgrade():
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



def downgrade():
    pass
