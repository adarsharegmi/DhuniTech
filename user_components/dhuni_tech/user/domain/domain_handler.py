from ml_backend.candidate.domain import model
from ml_backend.candidate.domain import command

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
                "first_name":cmd.name,
                "last_name":cmd.placement_name,
                "status":cmd.status
            }
        )