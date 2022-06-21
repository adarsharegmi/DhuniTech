from datetime import date
from typing import Optional
from enum import Enum
from pydantic import BaseModel, validator


class AddJob(BaseModel):
    job_title: str

class UpdateJob(BaseModel):
    id_: Optional[str]
    job_title: Optional[str]

    
class DeleteJob(BaseModel):
    id: str

class AddJobSkills(BaseModel):
    job_id: str
    skills_name: str



class UpdateJobSkills(BaseModel):
    id_: Optional[str]
    job_id: Optional[str]
    skills_name: Optional[str]

    
class DeleteJobSkills(BaseModel):
    id: str