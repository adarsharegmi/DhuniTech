import sqlalchemy as sa
from enum import Enum
from nepAddy_core.lib.repository import (
    Repository,
    SqlAlchemyRepository,
)
from nepAddy_core.lib.repository import DbConnection
from dhuni_tech.candidate.domain import model
from dhuni_tech.candidate.adapters.orm import (
    candidate, candidate_skills
)


class Candidate(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class CandidateRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(
        self,
        model: model.Candidate,
    ):
        candidate_query = candidate.insert()
        candidate_values = {
            "id": str(model.id_),
            "first_name":model.first_name,
            "last_name":model.last_name,
            "status":model.status
        }
        await self.db.execute(query=candidate_query, values=candidate_values)

    async def get(self, ref: str):
        candidate_query = sa.select(
            [
                candidate.c.id,
                candidate.c.first_name,
                candidate.c.last_name,
                candidate.c.status
            ]
        ).where(candidate.c.id == ref)
        candidate_data = await self.db.fetch_one(query=candidate_query)
        return candidate_data

    async def update(self, model: model.Candidate):
        update_candidate = candidate.update().where(candidate.c.id == str(model.id_))
        candidate_values = {
            "first_name":model.first_name,
            "last_name":model.last_name,
            "status":model.status,
        }
        await self.db.execute(
            query=update_candidate,
            values=candidate_values,
        )

        
    async def delete(self, id: str): 
        await self.db.execute(candidate.delete().where(candidate.c.id==str(id)))



class CandidateSkillsRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(
        self,
        model: model.CandidateSkills,
    ):
        candidate_skills_query = candidate_skills.insert()
        candidate_skills_values = {
            "id": str(model.id_),
            "candidate_id":model.candidate_id,
            "skills_name":model.skills_name.title()
        }
        await self.db.execute(query=candidate_skills_query, values=candidate_skills_values)

    async def get(self, ref: str):
        candidate_skills_query = sa.select(
            [
                candidate_skills.c.id,
                candidate_skills.c.candidate_id,
                candidate_skills.c.skills_name
            ]
        ).where(candidate_skills.c.id == ref)
        candidate_skills_data = await self.db.fetch_one(query=candidate_skills_query)
        return candidate_skills_data

    async def update(self, model: model.CandidateSkills):
        update_candidate_skills = candidate_skills.update().where(candidate_skills.c.id == str(model.id_))
        candidate_skills_values = {
            "candidate_id":model.candidate_id,
            "skills_name":model.skills_name,
        }
        await self.db.execute(
            query=update_candidate_skills,
            values=candidate_skills_values,
        )

        
    async def delete(self, id: str): 
        await self.db.execute(candidate_skills.delete().where(candidate_skills.c.id==str(id)))