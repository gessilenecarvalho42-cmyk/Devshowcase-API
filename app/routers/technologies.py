from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TechnologyCreate, TechnologyResponse
from app.repositories import technology_repository


router = APIRouter(
    prefix="/api/technologies",
    tags=["Technologies"]
)


@router.post(
    "/",
    response_model=TechnologyResponse,
    status_code=201
)
def create_technology(
    technology: TechnologyCreate,
    db: Session = Depends(get_db)
):
    return technology_repository.create_technology(
        db=db,
        tech=technology
    )


@router.get(
    "/",
    response_model=list[TechnologyResponse]
)
def list_technologies(
    db: Session = Depends(get_db)
):
    return technology_repository.get_all_technologies(db=db)