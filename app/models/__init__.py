# Este arquivo expõe todas as classes da pasta models para o resto da aplicação.
# Quando fazemos "from app.models import Profile", o Python vai olhar aqui primeiro.
from app.models.profile import Profile
from app.models.technology import Technology
from app.models.project import Project, project_technology
from app.models.feedback import Feedback
