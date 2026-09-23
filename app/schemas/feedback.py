from pydantic import BaseModel, Field


class FeedbackCreate(BaseModel):
    rating: int = Field(
        ...,
        ge=1,
        le=5,
        description="A nota deve ser entre 1 e 5"
    )
    comment: str | None = None


class FeedbackResponse(BaseModel):
    id: int
    rating: int
    comment: str | None
    project_id: int

    class Config:
        from_attributes = True