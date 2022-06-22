import sqlalchemy as sa
from enum import Enum
from nepAddy_core.lib.repository import (
    Repository,
    SqlAlchemyRepository,
)
from nepAddy_core.lib.repository import DbConnection
from dhuni_tech.job.domain import model
from dhuni_tech.job.adapters.orm import (
    job, job_skills
)


class Job(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class JobRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(
        self,
        model: model.Job,
    ):
        job_query = job.insert()
        job_values = {
            "id": str(model.id_),
            "job_title":model.job_title.title(),
        }
        await self.db.execute(query=job_query, values=job_values)

    async def get(self, ref: str):
        job_query = sa.select(
            [
                job.c.id,
                job.c.job_title,
            ]
        ).where(job.c.id == ref)
        job_data = await self.db.fetch_one(query=job_query)
        return job_data

    async def update(self, model: model.Job):
        update_job = job.update().where(job.c.id == str(model.id_))
        job_values = {
            "job_title":model.job_title.title(),
        }
        await self.db.execute(
            query=update_job,
            values=job_values,
        )

        
    async def delete(self, id: str): 
        await self.db.execute(job.delete().where(job.c.id==str(id)))



class JobSkillsRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(
        self,
        model: model.JobSkills,
    ):
        job_skills_query = job_skills.insert()
        job_skills_values = {
            "id": str(model.id_),
            "job_id":model.job_id,
            "skills_name":model.skills_name.title()
        }
        await self.db.execute(query=job_skills_query, values=job_skills_values)

    async def get(self, ref: str):
        job_skills_query = sa.select(
            [
                job_skills.c.id,
                job_skills.c.job_id,
                job_skills.c.skills_name
            ]
        ).where(job_skills.c.id == ref)
        job_skills_data = await self.db.fetch_one(query=job_skills_query)
        return job_skills_data

    async def update(self, model: model.JobSkills):
        update_job_skills = job_skills.update().where(job_skills.c.id == str(model.id_))
        job_skills_values = {
            "job_id":model.job_id,
            "skills_name":model.skills_name,
        }
        await self.db.execute(
            query=update_job_skills,
            values=job_skills_values,
        )

        
    async def delete(self, id: str): 
        await self.db.execute(job_skills.delete().where(job_skills.c.id==str(id)))