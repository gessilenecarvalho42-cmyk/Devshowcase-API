from pydantic import BaseModel, HttpUrl, Field
from typing import Optional


class ProjectBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        description="O título não pode ser vazio"
    )

    description: str = Field(
        ...,
        min_length=1,
        description="A descrição não pode ser vazia"
    )

    url: Optional[HttpUrl] = None

    profile_id: int


class ProjectCreate(ProjectBase):
    technology_ids: list[int] = []


class ProjectResponse(ProjectBase):
    id: int
    average_rating: float = 0.0
    upvotes: int = 0

    class Config:
        from_attributes = True