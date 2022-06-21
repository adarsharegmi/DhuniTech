from uuid import UUID
import sqlalchemy as sa
from dhuni_tech.candidate.adapters.orm import (
    candidate,
)
from nepAddy_core.lib.db_connection import DbConnection

async def get_candidate(id_: UUID, db: DbConnection):
    candidate_query = sa.select(
        [
            candidate.c.id,
            candidate.c.first_name,
            candidate.c.last_name,
            candidate.c.status,
        ]
    )
    candidate_result = await db.fetch_one(query=candidate_query)
    return candidate_result




async def get_all_candidate(db: DbConnection):
    candidate_query = sa.select(
        [
            candidate.c.id,
            candidate.c.first_name,
            candidate.c.last_name,
            candidate.c.status,
        ]
    )
    candidate_result = await db.fetch_all(query=candidate_query)
    return candidate_result


async def get_candidate_skills(id_: UUID, db: DbConnection):
    candidate_skills_query = sa.select(
        [
            candidate_skills.c.id,
            candidate_skills.c.skills_name
        ]
    )
    candidate_skills_result = await db.fetch_one(query=candidate_skills_query)
    return candidate_skills_result




async def get_all_candidate_skills(db: DbConnection):
    candidate_skills_query = sa.select(
        [
            candidate_skills.c.id,
            candidate_skills.c.skills_name
        ]
    )
    candidate_skills_result = await db.fetch_all(query=candidate_skills_query)
    return candidate_skills_result