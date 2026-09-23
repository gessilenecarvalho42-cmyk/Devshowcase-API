from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.project import project_technology

# Tabela Technology (Tecnologias, ex: Python, Java)
class Technology(Base):
    __tablename__ = "technologies"
    
    # Colunas
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False) # Nome único (não pode repetir)

    # Relacionamento N:N inverso com Projetos, indicando a tabela secundária
    projects = relationship("Project", secondary=project_technology, back_populates="technologies")
