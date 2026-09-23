# DevShowcase API

API RESTful desenvolvida em **Python** utilizando **FastAPI** e **SQLite**. Projeto desenvolvido para gerenciar perfis de desenvolvedores, seus projetos e tecnologias.

## Tecnologias Utilizadas
- **Python** 
- **FastAPI** (Framework web)
- **SQLite** (Banco de dados relacional)
- **SQLAlchemy** (ORM)
- **Pydantic** (Validação de DTOs)
- **Uvicorn** (Servidor ASGI)

## Estrutura do projeto
O projeto segue o padrão de **Camadas de Acesso a Dados**:
- `app/models/`: Entidades de domínio (Profile, Project, Feedback, Technology) e mapeamento relacional.
- `app/schemas/`: DTOs de entrada e saída com validação de campos obrigatórios.
- `app/repositories/`: Classes responsáveis pelas operações de persistência no banco de dados.
- `app/routers/`: Controladores responsáveis pelos endpoints REST.
- `app/database.py`: Configuração de conexão do banco de dados SQLAlchemy.
- `app/main.py`: Arquivo raiz da aplicação.

## Como Executar o Projeto

1. Clone o repositório ou abra a pasta do projeto.
2. Crie um ambiente virtual na raiz do projeto:
   ```bash
   python -m venv .venv
   ```
3. Ative o ambiente virtual (no Windows):
   ```bash
   .venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Inicie a aplicação com o Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```

A API estará disponível em: `http://127.0.0.1:8000`.

## Documentação e Endpoints
O FastAPI gera automaticamente a documentação interativa (Swagger UI) para testes rápidos. 
Acesse no navegador: `http://127.0.0.1:8000/docs`

Os principais endpoints implementados são:
- `POST /api/profiles` - Cadastro de perfil
- `GET /api/profiles/{id}` - Busca perfil por ID
- `POST /api/technologies` - Cadastro de tecnologia
- `GET /api/technologies` - Listagem de todas as tecnologias
- `POST /api/projects` - Cadastro de projeto
- `GET /api/projects` - Listagem de projetos
