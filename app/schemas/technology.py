from pydantic import BaseModel, Field

# Base DTO para Technology
class TechnologyBase(BaseModel):
    name: str = Field(..., min_length=1, description="O nome da tecnologia não pode ser vazio")

# DTO usado no POST
class TechnologyCreate(TechnologyBase):
    pass

# DTO usado no GET
class TechnologyResponse(TechnologyBase):
    id: int # Inclui o ID gerado pelo banco
    class Config:
        from_attributes = True
