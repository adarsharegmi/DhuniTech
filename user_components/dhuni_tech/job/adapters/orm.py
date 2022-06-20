from __future__ import annotations
import logging
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy_utils import EmailType


SQLMETADATA = sa.MetaData()

logger = logging.getLogger(__name__)
job = sa.Table(
    "Job",
    SQLMETADATA,
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


job_skills = sa.Table(
    "JobSkills",
    SQLMETADATA,
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