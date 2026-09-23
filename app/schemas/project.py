from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

# Base DTO para Project, definindo as propriedades essenciais e validações
class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, description="O título não pode ser vazio")
    description: str = Field(..., min_length=1)
    url: Optional[HttpUrl] = None # Valida se é uma URL completa e válida (https://...)
    profile_id: int  # Precisa obrigatoriamente referenciar qual o ID do perfil dono

# DTO para envio de dados na criação
class ProjectCreate(ProjectBase):
    pass

# DTO de resposta formatando a saída JSON
class ProjectResponse(ProjectBase):
    id: int # Inclui o ID salvo no banco
    class Config:
        from_attributes = True
