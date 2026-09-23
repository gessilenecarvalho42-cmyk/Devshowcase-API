from pydantic import BaseModel, Field

# Base DTO para Feedbacks
class FeedbackBase(BaseModel):
    comment: str = Field(..., min_length=1, description="O comentário não pode ser vazio")
    project_id: int # A qual projeto este feedback pertence

# DTO para a criação de feedbacks
class FeedbackCreate(FeedbackBase):
    pass

# DTO de retorno na listagem de feedbacks
class FeedbackResponse(FeedbackBase):
    id: int
    class Config:
        from_attributes = True
