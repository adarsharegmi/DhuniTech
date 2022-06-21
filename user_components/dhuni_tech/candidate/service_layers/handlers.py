from __future__ import annotations
from sanic import Sanic
from dhuni_tech.candidate.adapters import repository
from dhuni_tech.candidate.domain import command, domain_handler, model
from dhuni_tech.candidate.service_layers import unit_of_work
from dhuni_tech.candidate.views import views


err = []
def check_app():
    try:
        app = Sanic.get_app("DhuniTech")
    except Exception:
        app = Sanic("DhuniTech")
    return app

async def add_candidate(
    cmd: command.AddCandidate,
    uow: unit_of_work.CandidateSqlAlchemyUnitOfWork,
):
    async with uow:
        app = check_app()
        candidate = await domain_handler.add_candidate(cmd)
        await uow.repository.add(candidate)
    return candidate.id_


async def update_candidate(
    cmd: command.UpdateCandidate,
    uow: unit_of_work.CandidateSqlAlchemyUnitOfWork,
):
    async with uow:
        candidate = await uow.repository.get(cmd.id_)
        app = check_app()
        candidate = model.Candidate(
            id_=candidate["id"],
            first_name=candidate["first_name"],
            last_name=candidate["last_name"],
            status=candidate["status"]
        )
        candidate_command = command.UpdateCandidate(
            candidate=candidate,
            id_=str(candidate.id_),
            first_name=cmd.first_name if cmd.first_name else candidate.first_name,
            last_name = cmd.last_name if cmd.last_name else candidate.last_name,
            status = cmd.status if cmd.status else candidate.status,
            
        )
        candidate = await domain_handler.update_candidate(cmd=candidate_command)
        await uow.repository.update(candidate)


async def delete_candidate(
    cmd:command.DeleteCandidate,
    uow: unit_of_work.CandidateSqlAlchemyUnitOfWork,
):
    await uow.repository.delete(cmd.id)



async def add_candidate_skills(
    cmd: command.AddCandidateSkills,
    uow: unit_of_work.CandidateSkillsSqlAlchemyUnitOfWork,
):
    async with uow:
        app = check_app()
        candidate_skills = await domain_handler.add_candidate_skills(cmd)
        await uow.repository.add(candidate_skills)
    return candidate_skills.id_


async def update_candidate_skills(
    cmd: command.UpdateCandidateSkills,
    uow: unit_of_work.CandidateSkillsSqlAlchemyUnitOfWork,
):
    async with uow:
        candidate_skills = await uow.repository.get(cmd.id_)
        app = check_app()
        candidate_skills = model.CandidateSkills(
            id_=candidate_skills["id"],
            skills_name=candidate_skills["skills_name"]
        )
        candidate_skills_command = command.UpdateCandidateSkills(
            candidate_skills=candidate_skills,
            id_=str(candidate_skills.id_),
            skills_name=cmd.skills_name if cmd.skills_name else candidate_skills.skills_name
            
        )
        candidate_skills = await domain_handler.update_candidate_skills(cmd=candidate_skills_command)
        await uow.repository.update(candidate_skills)


async def delete_candidate_skills(
    cmd:command.DeleteCandidateSkills,
    uow: unit_of_work.CandidateSkillsSqlAlchemyUnitOfWork,
):
    await uow.repository.delete(cmd.id)