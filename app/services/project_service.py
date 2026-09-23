from sqlalchemy.orm import Session

from app.models.feedback import Feedback
from app.repositories import project_repository
from app.schemas.feedback import FeedbackCreate


def create_feedback(
    db: Session,
    project_id: int,
    feedback_data: FeedbackCreate
):
    # Verifica se o projeto existe
    project = project_repository.get_project(
        db=db,
        project_id=project_id
    )

    if not project:
        return None

    # Cria o feedback
    feedback = Feedback(
        rating=feedback_data.rating,
        comment=feedback_data.comment,
        project_id=project_id
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    # Calcula a média das avaliações
    project = project_repository.update_average_rating(
        db=db,
        project_id=project_id
    )

    return feedback

def upvote_project(
    db: Session,
    project_id: int
):
    project = project_repository.get_project(
        db=db,
        project_id=project_id
    )

    if not project:
        return None

    project.upvotes += 1

    db.commit()
    db.refresh(project)

    return project