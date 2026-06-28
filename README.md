# Petshop Pro Fastapi

API REST construída com FastAPI + SQLAlchemy + PostgreSQL.

## Tecnologias

- Python 3.12 / FastAPI 0.111
- SQLAlchemy 2.0 + PostgreSQL (SQLite em dev)
- Pydantic v2
- Docker + docker-compose

## Rodar localmente

```bash
docker-compose up --build
# API: http://localhost:8080
# Swagger: http://localhost:8080/docs
# Health: http://localhost:8080/actuator/health
```

## Endpoints

| Método   | Rota                    | Descrição                       |
|----------|-------------------------|---------------------------------|
| `GET`    | `/api/pets/`          | Listar (paginado + filtro nome) |
| `GET`    | `/api/pets/{id}`      | Buscar por ID                   |
| `POST`   | `/api/pets/`          | Criar                           |
| `PUT`    | `/api/pets/{id}`      | Atualizar                       |
| `DELETE` | `/api/pets/{id}`      | Deletar                         |
| `GET`    | `/api/donos/`          | Listar (paginado + filtro nome) |
| `GET`    | `/api/donos/{id}`      | Buscar por ID                   |
| `POST`   | `/api/donos/`          | Criar                           |
| `PUT`    | `/api/donos/{id}`      | Atualizar                       |
| `DELETE` | `/api/donos/{id}`      | Deletar                         |
| `GET`    | `/api/consultas/`          | Listar (paginado + filtro nome) |
| `GET`    | `/api/consultas/{id}`      | Buscar por ID                   |
| `POST`   | `/api/consultas/`          | Criar                           |
| `PUT`    | `/api/consultas/{id}`      | Atualizar                       |
| `DELETE` | `/api/consultas/{id}`      | Deletar                         |
| `GET`    | `/api/produtos/`          | Listar (paginado + filtro nome) |
| `GET`    | `/api/produtos/{id}`      | Buscar por ID                   |
| `POST`   | `/api/produtos/`          | Criar                           |
| `PUT`    | `/api/produtos/{id}`      | Atualizar                       |
| `DELETE` | `/api/produtos/{id}`      | Deletar                         |

## Paginação

```
GET /api/pacientes/?skip=0&limit=10
GET /api/pacientes/?nome=joao
GET /api/consultas/?paciente_id=1
```
