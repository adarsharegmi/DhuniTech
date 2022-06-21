from __future__ import annotations
from sanic import Sanic
from dhuni_tech.job.adapters import repository
from dhuni_tech.job.domain import command, domain_handler, model
from dhuni_tech.job.service_layers import unit_of_work
from dhuni_tech.job.views import views


err = []
def check_app():
    try:
        app = Sanic.get_app("DhuniTech")
    except Exception:
        app = Sanic("DhuniTech")
    return app

async def add_job(
    cmd: command.AddJob,
    uow: unit_of_work.JobSqlAlchemyUnitOfWork,
):
    async with uow:
        app = check_app()
        job = await domain_handler.add_job(cmd)
        await uow.repository.add(job)
    return job.id_


async def update_job(
    cmd: command.UpdateJob,
    uow: unit_of_work.JobSqlAlchemyUnitOfWork,
):
    async with uow:
        job = await uow.repository.get(cmd.id_)
        app = check_app()
        job = model.Job(
            id_=job["id"],
            job_title=job["job_title"]
        )
        job_command = command.UpdateJob(
            job=job,
            id_=str(job.id_),
            job_title=cmd.job_title if cmd.job_title else job.job_title
            
        )
        job = await domain_handler.update_job(cmd=job_command)
        await uow.repository.update(job)


async def delete_job(
    cmd:command.DeleteJob,
    uow: unit_of_work.JobSqlAlchemyUnitOfWork,
):
    await uow.repository.delete(cmd.id)




async def add_job_skills(
    cmd: command.AddJobSkills,
    uow: unit_of_work.JobSkillsSqlAlchemyUnitOfWork,
):
    async with uow:
        app = check_app()
        job_skills = await domain_handler.add_job_skills(cmd)
        await uow.repository.add(job_skills)
    return job_skills.id_


async def update_job_skills(
    cmd: command.UpdateJobSkills,
    uow: unit_of_work.JobSkillsSqlAlchemyUnitOfWork,
):
    async with uow:
        job_skills = await uow.repository.get(cmd.id_)
        app = check_app()
        job_skills = model.JobSkills(
            id_=job_skills["id"],
            skills_name=job_skills["skills_name"]
        )
        job_skills_command = command.UpdateJobSkills(
            job_skills=job_skills,
            id_=str(job_skills.id_),
            skills_name=cmd.skills_name if cmd.skills_name else job_skills.skills_name
            
        )
        job_skills = await domain_handler.update_job_skills(cmd=job_skills_command)
        await uow.repository.update(job_skills)


async def delete_job_skills(
    cmd:command.DeleteJobSkills,
    uow: unit_of_work.JobSkillsSqlAlchemyUnitOfWork,
):
    await uow.repository.delete(cmd.id)