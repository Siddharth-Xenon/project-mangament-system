from pydantic import BaseModel
from datetime import datetime


class ProjectBase(BaseModel):
    name: str
    description: str


class ProjectCreate(ProjectBase):
    pass


class ProjectResponse(ProjectBase):
    id: str
    created_by: str
    created_at: datetime

    class Config:
        from_attributes = True
