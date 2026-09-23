from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

# Tabela associativa N:N (Muitos para Muitos) entre Project e Technology
# Cria uma tabela no banco só para guardar qual projeto usa qual tecnologia
project_technology = Table(
    "project_technology",
    Base.metadata,
    Column("project_id", Integer, ForeignKey("projects.id")),
    Column("technology_id", Integer, ForeignKey("technologies.id"))
)

# Tabela Project (Projetos do perfil)
class Project(Base):
    __tablename__ = "projects" # Nome da tabela no banco
    
    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)        # Título obrigatório
    description = Column(Text, nullable=False)    # Descrição obrigatória
    url = Column(String, nullable=True)           # Link do projeto
    
    # Chave estrangeira ligando este projeto ao Perfil dono dele (Relação N:1)
    profile_id = Column(Integer, ForeignKey("profiles.id"))

    # Configuração dos relacionamentos para o SQLAlchemy entender a ponte entre tabelas
    profile = relationship("Profile", back_populates="projects")
    
    # Relacionamento Muitos para Muitos (N:N) usando a tabela associativa criada acima
    technologies = relationship("Technology", secondary=project_technology, back_populates="projects")
    
    # Relacionamento 1:N com Feedbacks (Um projeto tem várias opiniões)
    feedbacks = relationship("Feedback", back_populates="project")
