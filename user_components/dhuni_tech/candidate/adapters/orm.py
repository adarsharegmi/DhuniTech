from __future__ import annotations
import logging
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy_utils import EmailType


SQLMETADATA = sa.MetaData()

logger = logging.getLogger(__name__)
candidate = sa.Table(
    "Candidate",
    SQLMETADATA,
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



candidate_skills = sa.Table(
    "CandidateSkills",
    SQLMETADATA,
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