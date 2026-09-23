from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import (
    ProjectCreate,
    ProjectResponse,
    FeedbackCreate,
    FeedbackResponse
)
from app.repositories import project_repository
from app.services import project_service


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)


# Criar projeto
@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=201
)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    return project_repository.create_project(
        db=db,
        project=project
    )


# Listar projetos com filtro e paginação
@router.get(
    "/",
    response_model=list[ProjectResponse]
)
def get_projects(
    technology_id: int | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return project_repository.get_projects(
        db=db,
        technology_id=technology_id,
        page=page,
        limit=limit
    )


# Buscar projeto pelo ID
@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = project_repository.get_project(
        db=db,
        project_id=project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado."
        )

    return project


# Atualizar projeto
@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project(
    project_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    updated_project = project_repository.update_project(
        db=db,
        project_id=project_id,
        project_data=project
    )

    if not updated_project:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado."
        )

    return updated_project


# Cadastrar feedback
@router.post(
    "/{project_id}/feedbacks",
    response_model=FeedbackResponse,
    status_code=201
)
def create_feedback(
    project_id: int,
    feedback: FeedbackCreate,
    db: Session = Depends(get_db)
):
    feedback_created = project_service.create_feedback(
        db=db,
        project_id=project_id,
        feedback_data=feedback
    )

    if not feedback_created:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado."
        )

    return feedback_created


# Dar upvote no projeto
@router.put(
    "/{project_id}/upvote",
    response_model=ProjectResponse
)
def upvote_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = project_service.upvote_project(
        db=db,
        project_id=project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado."
        )

    return project