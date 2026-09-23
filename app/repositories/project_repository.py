from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.project import Project
from app.models.technology import Technology
from app.models.feedback import Feedback
from app.schemas.project import ProjectCreate
from app.schemas.feedback import FeedbackCreate


def create_project(db: Session, project: ProjectCreate):
    db_project = Project(
        title=project.title,
        description=project.description,
        url=str(project.url) if project.url else None,
        profile_id=project.profile_id,
        average_rating=0.0,
        upvotes=0
    )

    # Busca as tecnologias informadas
    if project.technology_ids:
        technologies = (
            db.query(Technology)
            .filter(Technology.id.in_(project.technology_ids))
            .all()
        )

        db_project.technologies = technologies

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_project(db: Session, project_id: int):
    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )


def update_project(
    db: Session,
    project_id: int,
    project_data: ProjectCreate
):
    project = get_project(db, project_id)

    if not project:
        return None

    project.title = project_data.title
    project.description = project_data.description
    project.url = (
        str(project_data.url)
        if project_data.url
        else None
    )
    project.profile_id = project_data.profile_id

    db.commit()
    db.refresh(project)

    return project


def create_feedback(
    db: Session,
    project_id: int,
    feedback_data: FeedbackCreate
):
    feedback = Feedback(
        rating=feedback_data.rating,
        comment=feedback_data.comment,
        project_id=project_id
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    # Calcula a média de todas as avaliações do projeto
    average = (
        db.query(func.avg(Feedback.rating))
        .filter(Feedback.project_id == project_id)
        .scalar()
    )

    project = get_project(db, project_id)

    if project:
        project.average_rating = float(average or 0)

        db.commit()
        db.refresh(project)

    return feedback


def upvote_project(db: Session, project_id: int):
    project = get_project(db, project_id)

    if not project:
        return None

    project.upvotes += 1

    db.commit()
    db.refresh(project)

    return project


def get_projects(
    db: Session,
    technology_id: int | None = None,
    page: int = 1,
    limit: int = 10
):
    query = db.query(Project)

    # Filtro por tecnologia
    if technology_id is not None:
        query = query.join(Project.technologies).filter(
            Project.technologies.any(id=technology_id)
        )

    # Paginação
    offset = (page - 1) * limit

    projects = (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )

    return projects

def update_average_rating(
    db: Session,
    project_id: int
):
    # Calcula a média das avaliações
    average = (
        db.query(func.avg(Feedback.rating))
        .filter(Feedback.project_id == project_id)
        .scalar()
    )

    project = get_project(db, project_id)

    if not project:
        return None

    project.average_rating = float(average or 0)

    db.commit()
    db.refresh(project)

    return project