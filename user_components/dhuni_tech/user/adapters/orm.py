from __future__ import annotations
import logging

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy_utils import EmailType


SQLMETADATA = sa.MetaData()

logger = logging.getLogger(__name__)
ai_model = sa.Table(
    "AIModel",
    SQLMETADATA,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column(
        "name",
        postgresql.UUID(as_uuid=False),
        ForeignKey("ModelRaw.id"),
    ),
    sa.Column(
        "placement_name",
        postgresql.UUID(as_uuid=False),
        ForeignKey("Placement.id"),
    ),
    sa.Column(
        "FileUpload",
        postgresql.UUID(as_uuid=False),
        ForeignKey("FileUpload.id"),
    ),
    sa.Column(
        "DBPull",
        postgresql.UUID(as_uuid=False),
        ForeignKey("DBPull.id"),
    ),
    sa.Column(
        "Streaming",
        postgresql.UUID(as_uuid=False),
        ForeignKey("Streaming.id"),
    ),
    sa.Column("source", sa.Enum("FileUpload", "DBPull", "Streaming", name="source_component")),
    sa.Column("effective_from", sa.String(255)),
    sa.Column("effective_to", sa.String(255)),
    sa.Column("status", sa.String(255)),
    sa.Column(
        "ai_model_status",
        sa.String(255),
    ),
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