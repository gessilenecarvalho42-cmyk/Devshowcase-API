from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ProjectCreate, ProjectResponse
from app.repositories import project_repository

# Roteador responsável pelos endpoints relacionados aos Projetos
router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)

# Endpoint para cadastrar projeto (POST)
# O parâmetro response_model formata o retorno como JSON e esconde coisas desnecessárias
@router.post("/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    # Chama a lógica salva no Repositório correspondente
    return project_repository.create_project(db=db, project=project)

# Endpoint para listar projetos (GET)
# Retorna uma lista [] de objetos do tipo ProjectResponse
@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return project_repository.get_all_projects(db)
