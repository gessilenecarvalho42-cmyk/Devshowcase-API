# Expõe as classes de validação DTO (Pydantic) de todos os arquivos, 
# para que o restante da aplicação as acesse mais facilmente.
from app.schemas.profile import ProfileCreate, ProfileResponse
from app.schemas.technology import TechnologyCreate, TechnologyResponse
from app.schemas.project import ProjectCreate, ProjectResponse
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
