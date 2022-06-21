from dhuni_tech.job.domain.command import (
    AddJob,
    UpdateJob,
    DeleteJob,
    AddJobSkills,
    UpdateJobSkills,
    DeleteJobSkills,
)
from dhuni_tech.job.service_layers.handlers import (
    add_job,
    update_job,
    delete_job,
    add_job_skills,
    update_job_skills,
    delete_job_skills,
)

from dhuni_tech.candidate.domain.command import (
    AddCandidate,
    UpdateCandidate,
    DeleteCandidate,
    AddCandidateSkills,
    UpdateCandidateSkills,
    DeleteCandidateSkills,
)
from dhuni_tech.candidate.service_layers.handlers import (
    add_candidate,
    update_candidate,
    delete_candidate,
    add_candidate_skills,
    update_candidate_skills,
    delete_candidate_skills,
)


COMMAND_HANDLERS = {
    AddJob: add_job,
    UpdateJob: update_job,
    DeleteJob: delete_job,
    AddJobSkills: add_job_skills,
    UpdateJobSkills: update_job_skills,
    DeleteJobSkills: delete_job_skills,
    AddCandidate:add_candidate,
    UpdateCandidate:update_candidate,
    DeleteCandidate: delete_candidate,
    AddCandidateSkills: add_candidate_skills,
    UpdateCandidateSkills: update_candidate_skills,
    DeleteCandidateSkills: delete_candidate_skills
}