from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Configuração da URL do banco de dados (SQLite local)
# "sqlite:///./devshowcase.db" cria um arquivo na raiz do projeto.
DATABASE_URL = "sqlite:///./devshowcase.db"

# Engine faz a comunicação do SQLAlchemy com o banco de dados.
# connect_args={"check_same_thread": False} é necessário apenas no SQLite para rodar com FastAPI.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criador de sessões: cada vez que a API for chamada, abrimos uma "SessionLocal" com o banco.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe base a partir da qual todos os modelos (tabelas) vão herdar
class Base(DeclarativeBase):
    pass

# Função utilitária que entrega a conexão com o banco (usada como dependência nas rotas)
def get_db():
    db = SessionLocal() # Abre a conexão
    try:
        yield db        # Entrega a conexão para quem pediu
    finally:
        db.close()      # Fecha a conexão após o uso