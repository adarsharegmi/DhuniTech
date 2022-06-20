from ml_backend.candidate.domain import model
from nepAddy_core.lib.command import Command
from typing import Optional


class AddCandidate(Command):
    first_name: str
    last_name: str
    status: str


class UpdateCandidateCommand(Command):
    candidate: model.Candidate = None


class UpdateCandidate(UpdateCandidateCommand):
    first_name: Optional[str]
    last_name: Optional[str]
    status: Optional[str]


class CandidateStatus(str, Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"
    archive = "ARCHIVE"


class ChangeCandidateStatus(Command):
    id_: str
    status: CandidateStatus
    
class DeleteCandidate(Command):
    id: str


class AddCandidateSkills(Command):
    candidate_id: str
    skills_name: str


class UpdateCandidateSkillsCommand(Command):
    candidate: model.CandidateSkills = None



class UpdateCandidateSkills(UpdateCandidateSkillsCommand):
    candidate_id: Optional[str]
    skills_name: Optional[str]

    
class DeleteCandidateSkills(Command):
    id: str