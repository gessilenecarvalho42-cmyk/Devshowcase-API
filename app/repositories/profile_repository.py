from sqlalchemy.orm import Session
from app.models import Profile
from app.schemas import ProfileCreate

# Camada de Acesso a Dados: Toda a regra de inserção e consulta ao banco fica aqui.

# Função para criar e salvar um perfil no banco
def create_profile(db: Session, profile: ProfileCreate):
    # Transforma o DTO do Pydantic em um Modelo SQLAlchemy
    db_profile = Profile(
        name=profile.name, 
        email=profile.email, 
        # Convertemos a URL validada para string antes de salvar no banco
        github_url=str(profile.github_url) if profile.github_url else None
    )
    # Adiciona a operação de inserção e efetiva no banco
    db.add(db_profile)
    db.commit()
    # Atualiza a instância para pegar dados gerados automaticamente (como o ID)
    db.refresh(db_profile)
    return db_profile

# Função para buscar um perfil no banco com base no ID fornecido
def get_profile(db: Session, profile_id: int):
    # Faz uma "query" buscando na tabela Profile onde o ID bate com o profile_id
    return db.query(Profile).filter(Profile.id == profile_id).first()
