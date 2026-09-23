from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database import Base, engine
from app.models import Profile, Technology, Project, Feedback
from app.routers import profiles, technologies, projects


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="DevShowcase API",
    description="API REST para gerenciamento de perfis, projetos e tecnologias."
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": exc.status_code,
            "error": exc.detail
        }
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status": 400,
            "error": "Erro de validação nos dados enviados.",
            "details": exc.errors()
        }
    )


app.include_router(profiles.router)
app.include_router(technologies.router)
app.include_router(projects.router)