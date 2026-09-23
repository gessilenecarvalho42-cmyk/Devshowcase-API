from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Tabela Feedback (Opinião sobre um projeto)
class Feedback(Base):
    __tablename__ = "feedbacks"
    
    # Colunas
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text, nullable=False) # Texto do comentário obrigatório
    
    # Chave estrangeira ligando à tabela de Projetos (N:1)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Relacionamento de volta para o Projeto
    project = relationship("Project", back_populates="feedbacks")
