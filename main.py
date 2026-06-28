from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import models
from database import engine
from routers import pet
from routers import dono
from routers import consulta
from routers import produto

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="petshop-pro-fastapi API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pet.router)
app.include_router(dono.router)
app.include_router(consulta.router)
app.include_router(produto.router)


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


@app.get("/actuator/health")
def health():
    return {"status": "UP", "service": "petshop-pro-fastapi"}
