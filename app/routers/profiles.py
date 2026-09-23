from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ProfileCreate, ProfileResponse
from app.repositories import profile_repository

# Define o roteador para a entidade Profile
router = APIRouter(
    prefix="/api/profiles",
    tags=["Profiles"]
)

# Endpoint para criar um novo perfil (POST)
@router.post("/", response_model=ProfileResponse, status_code=201)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    # Chama o repositório para salvar no banco de dados
    return profile_repository.create_profile(db=db, profile=profile)

# Endpoint para buscar um perfil pelo ID (GET)
@router.get("/{id}", response_model=ProfileResponse)
def get_profile(id: int, db: Session = Depends(get_db)):
    # Chama o repositório para buscar os dados
    db_profile = profile_repository.get_profile(db, profile_id=id)
    
    # Se não encontrar, retorna erro 404
    if not db_profile:
        raise HTTPException(status_code=404, detail="Perfil não encontrado")
    
    return db_profile
