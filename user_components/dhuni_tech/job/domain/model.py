from __future__ import annotations
import uuid
from typing import Any, Dict
from pydantic import BaseModel as Model

class Job(Model):
    id_: uuid.UUID
    job_title: str

    class Config:
        extra = "forbid"
        allow_mutation = True
        title = "job"
        arbitrary_types_allowed = True

    async def add_user_id(self, id: uuid.UUID):
        self.id_ = id

    async def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def __hash__(self):
        return hash(self.name)


async def job_factory(
    job_title: str
) -> Job:
    return Job(
        id_=uuid.uuid4(),
        job_title=job_title
    )



class JobSkills(Model):
    id_: uuid.UUID
    job_id: str
    skills_name: str

    class Config:
        extra = "forbid"
        allow_mutation = True
        title = "job_skills"
        arbitrary_types_allowed = True

    async def add_job_skills_id(self, id: uuid.UUID):
        self.id_ = id

    async def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def __hash__(self):
        return hash(self.name)


async def job_skills_factory(
    job_id: str,
    skills_name: str
) -> JobSkills:
    return JobSkills(
        id_=uuid.uuid4(),
        job_id=job_id,
        skills_name=skills_name
    )
