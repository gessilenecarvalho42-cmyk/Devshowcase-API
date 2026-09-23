from sqlalchemy.orm import Session
from app.models import Technology
from app.schemas import TechnologyCreate

# Camada de Acesso a Dados para as Tecnologias

# Salva uma nova tecnologia no banco
def create_technology(db: Session, tech: TechnologyCreate):
    db_tech = Technology(name=tech.name)
    db.add(db_tech)
    db.commit()
    db.refresh(db_tech)
    return db_tech

# Busca e lista todas as tecnologias cadastradas
def get_all_technologies(db: Session):
    return db.query(Technology).order_by(Technology.id).all()
