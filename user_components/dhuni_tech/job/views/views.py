from uuid import UUID
import sqlalchemy as sa
from dhuni_tech.job.adapters.orm import (
    job,job_skills
)
from nepAddy_core.lib.db_connection import DbConnection

async def get_job(id_: UUID, db: DbConnection):
    job_query = sa.select(
        [
            job.c.id,
            job.c.job_title
        ]
    ).where(job.c.id==str(id_))
    job_result = await db.fetch_one(query=job_query)
    return job_result




async def get_all_job(db: DbConnection):
    job_query = sa.select(
        [
            job.c.id,
            job.c.job_title
        ]
    )
    job_result = await db.fetch_all(query=job_query)
    return job_result


async def get_job_skills(id_: UUID, db: DbConnection):
    job_skills_query = sa.select(
        [
            job_skills.c.id,
            job_skills.c.job_id,
            job_skills.c.skills_name,
            job.c.job_title,
        ]
    ).where(sa.and_(job_skills.c.job_id==str(id_), job_skills.c.job_id==job.c.id))
    job_skills_result = await db.fetch_all(query=job_skills_query)
    return job_skills_result




async def get_all_job_skills(db: DbConnection):
    job_skills_query = sa.select(
        [
            job_skills.c.id,
            job_skills.c.job_id,
            job_skills.c.skills_name,
            job.c.job_title
        ]
    ).where(sa.and_( job.c.id==job_skills.c.job_id))
    job_skills_result = await db.fetch_all(query=job_skills_query)
    return job_skills_result

    #.where(sa.and_(job.c.id==job_skills.c.job_id))