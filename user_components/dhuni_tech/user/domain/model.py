from __future__ import annotations
import uuid
from typing import Any, Dict
from pydantic import BaseModel as Model

class Candidate(Model):
    id_: uuid.UUID
    first_name: str
    last_name: str
    status: str

    class Config:
        extra = "forbid"
        allow_mutation = True
        title = "candidate"
        arbitrary_types_allowed = True

    async def add_user_id(self, id: uuid.UUID):
        self.id_ = id

    async def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def __hash__(self):
        return hash(self.name)


async def candidate_factory(
    first_name: str,
    last_name: str,
    status: str
) -> Candidate:
    return Candidate(
        id_=uuid.uuid4(),
        first_name=first_name,
        last_name=last_name,
        status=status
    )
