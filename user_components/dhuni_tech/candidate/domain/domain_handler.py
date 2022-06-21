from dhuni_tech.candidate.domain import model
from dhuni_tech.candidate.domain import command

async def add_candidate(cmd: command.AddCandidate) -> model.Candidate:
    return await model.candidate_factory(
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        status=cmd.status
    )


async def update_candidate(
    cmd: command.UpdateCandidateCommand,
) -> model.Candidate:
    if isinstance(cmd, command.UpdateCandidate):
        return await cmd.candidate.update(
            {
                "candidate_id":cmd.candidate_id,
                "skills_name":cmd.skills_name
            }
        )

async def add_candidate_skills(cmd: command.AddCandidateSkills) -> model.CandidateSkills:
    return await model.candidate_skills_factory(
        candidate_id=cmd.candidate_id,
        skills_name=cmd.skills_name
    )


async def update_candidate_skills(
    cmd: command.UpdateCandidateCommand,
) -> model.CandidateSkills:
    if isinstance(cmd, command.UpdateCandidateSkills):
        return await cmd.candidate_skills.update(
            {
                "candidate_id":cmd.candidate_id,
                "skills_name":cmd.skills_name
            }
        )