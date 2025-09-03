from pydantic import BaseModel
from typing import Dict


class ReaderData(BaseModel):
    id: str
    preferable: list[str]
    unacceptable: list[str]
    conflict: list[str]
    capacity: int


class RpaMatchingInput(BaseModel):
    allProjects: list[str]
    allReaders: list[ReaderData]


class RpaMatchingPair(BaseModel):
    readerId: str
    projectId: str


class RpaMatchingOutput(BaseModel):
    assignments: list[RpaMatchingPair]
    unassignedProjects: list[str]
    load: Dict[str, int]
