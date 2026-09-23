from fastapi import FastAPI
from app.database import Base, engine
from app.routers import profiles, technologies, projects

# Cria as tabelas no banco de dados SQLite baseadas nos modelos definidos
Base.metadata.create_all(bind=engine)

# Instancia a aplicação FastAPI
app = FastAPI(
    title="DevShowcase API",
    description="API para gerenciamento de perfis, projetos e tecnologias."
)

# Rota raiz simples para testar se a API está no ar
@app.get("/")
def root():
    return {"message": "DevShowcase API funcionando!"}

# Inclui as rotas separadas por entidades (Controllers/Endpoints)
app.include_router(profiles.router)
app.include_router(technologies.router)
app.include_router(projects.router)