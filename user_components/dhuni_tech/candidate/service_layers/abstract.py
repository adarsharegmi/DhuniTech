from datetime import date
from typing import Optional
from enum import Enum
from pydantic import BaseModel, validator
from pyparsing import Opt


class AddCandidate(BaseModel):
    first_name: str
    last_name: str
    status: str

class UpdateCandidate(BaseModel):
    id_: Optional[str]
    first_name: Optional[str]
    last__name: Optional[str]
    status: Optional[str]

class CandidateStatus(str, Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"
    archive = "ARCHIVE"
    
class DeleteCandidate(BaseModel):
    id: str

class AddCandidateSkills(BaseModel):
    candidate_id: str
    skills_name: str



class UpdateCandidateSkills(BaseModel):
    candidate_id: Optional[str]
    skills_name: Optional[str]

    
class DeleteCandidateSkills(BaseModel):
    id: str