from dhuni_tech.job.domain import model
from nepAddy_core.lib.command import Command
from typing import Optional


class AddJob(Command):
    job_title: str


class UpdateJobCommand(Command):
    job: model.Job = None


class UpdateJob(UpdateJobCommand):
    id_: Optional[str]
    job_title: Optional[str]
    
class DeleteJob(Command):
    id: str


class AddJobSkills(Command):
    job_id: str
    skills_name: str


class UpdateJobSkillsCommand(Command):
    job: model.JobSkills = None



class UpdateJobSkills(UpdateJobSkillsCommand):
    id_: Optional[str]
    job_id: Optional[str]
    skills_name: Optional[str]

    
class DeleteJobSkills(Command):
    id: str