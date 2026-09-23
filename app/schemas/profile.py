from pydantic import BaseModel, HttpUrl, EmailStr, Field
from typing import Optional

# Base DTO (Data Transfer Object) para Profile
# Aqui são definidas as regras de validação para a API (ex: tipo email e formato URL)
class ProfileBase(BaseModel):
    name: str = Field(..., min_length=1, description="O nome não pode ser vazio")
    email: EmailStr # Valida formato xyz@abc.com
    github_url: Optional[HttpUrl] = None # Valida se é uma URL válida (ex: https://...)

# DTO usado quando um perfil é CRIADO (entrada de dados)
class ProfileCreate(ProfileBase):
    pass # Herda tudo do Base, não precisa de mais nada por enquanto

# DTO usado quando a API RETORNA o perfil salvo (saída de dados)
class ProfileResponse(ProfileBase):
    id: int # Quando retorna do banco, já tem o ID
    
    class Config:
        # Permite que o Pydantic converta objetos do SQLAlchemy em JSON
        from_attributes = True
