from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

# Tabela Profile (Perfil do Desenvolvedor)
class Profile(Base):
    __tablename__ = "profiles" # Nome da tabela no banco
    
    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True) # ID principal
    name = Column(String, nullable=False)              # Nome não pode ser vazio
    email = Column(String, unique=True, index=True, nullable=False) # Email deve ser único
    github_url = Column(String, nullable=True)         # URL do GitHub pode ser nula (opcional)

    # Relacionamento 1:N com a tabela de projetos (Um perfil tem vários projetos)
    projects = relationship("Project", back_populates="profile")
