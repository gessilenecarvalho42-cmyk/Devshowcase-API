from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import TechnologyCreate, TechnologyResponse
from app.repositories import technology_repository

# Roteador responsável pelos endpoints de Tecnologias
router = APIRouter(
    prefix="/api/technologies",
    tags=["Technologies"]
)

# Endpoint para cadastrar uma tecnologia nova (POST)
@router.post("/", response_model=TechnologyResponse, status_code=201)
def create_technology(tech: TechnologyCreate, db: Session = Depends(get_db)):
    return technology_repository.create_technology(db=db, tech=tech)

# Endpoint para listar todas as tecnologias (GET)
@router.get("/", response_model=list[TechnologyResponse])
def get_technologies(db: Session = Depends(get_db)):
    return technology_repository.get_all_technologies(db)
