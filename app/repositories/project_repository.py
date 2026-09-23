from sqlalchemy.orm import Session
from app.models import Project
from app.schemas import ProjectCreate

# Camada de Acesso a Dados para os Projetos

# Cria e insere um projeto no banco
def create_project(db: Session, project: ProjectCreate):
    # Instancia o modelo SQLAlchemy a partir dos dados validados
    db_project = Project(
        title=project.title, 
        description=project.description, 
        url=str(project.url) if project.url else None, 
        profile_id=project.profile_id
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Retorna uma lista com todos os projetos do banco
def get_all_projects(db: Session):
    return db.query(Project).all()
