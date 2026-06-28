from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class PetBase(BaseModel):
    nome: str
    especie: Optional[str] = None
    raca: Optional[str] = None
    peso: float

class PetCreate(PetBase):
    pass

class PetUpdate(PetBase):
    pass

class PetResponse(PetBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class DonoBase(BaseModel):
    nome: str
    email: str
    cpf: str
    telefone: str

class DonoCreate(DonoBase):
    pass

class DonoUpdate(DonoBase):
    pass

class DonoResponse(DonoBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ConsultaBase(BaseModel):
    pet_id: Optional[int] = None
    dono_id: Optional[int] = None
    data: Optional[datetime] = None
    diagnostico: str
    status: str
    observacoes: Optional[str] = None

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(ConsultaBase):
    pass

class ConsultaResponse(ConsultaBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ProdutoBase(BaseModel):
    nome: str
    preco: float
    estoque: int
    categoria: str

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

