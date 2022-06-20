from ml_backend.job.domain import model
from ml_backend.job.domain import command

async def add_job(cmd: command.AddJob) -> model.Job:
    return await model.job_factory(
        job_title=cmd.job_title,
    )


async def update_job(
    cmd: command.UpdateJobCommand,
) -> model.Job:
    if isinstance(cmd, command.UpdateJob):
        return await cmd.job.update(
            {
                "job_title":cmd.job_title
            }
        )


async def add_job_skills(cmd: command.AddJobSkills) -> model.JobSkills:
    return await model.job_skills_factory(
        job_id=cmd.job_id,
        skills_name=cmd.skills_name
    )


async def update_job_skills(
    cmd: command.UpdateJobCommand,
) -> model.JobSkills:
    if isinstance(cmd, command.UpdateJobSkills):
        return await cmd.job_skills.update(
            {
                "job_id":cmd.job_id,
                "skills_name":cmd.skills_name
            }
        )