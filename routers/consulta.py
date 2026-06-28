from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
import crud
from schemas import ConsultaCreate, ConsultaUpdate, ConsultaResponse

router = APIRouter(prefix="/api/consultas", tags=["consultas"])


@router.get('/', response_model=List[ConsultaResponse])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), pet_id: Optional[int] = None, dono_id: Optional[int] = None):
    items = crud.get_all_consulta(db, skip=skip, limit=limit)
    if pet_id is not None:
        items = [i for i in items if getattr(i, 'pet_id', None) == pet_id]
    if dono_id is not None:
        items = [i for i in items if getattr(i, 'dono_id', None) == dono_id]
    return items


@router.get('/{item_id}', response_model=ConsultaResponse)
def buscar(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_consulta(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Nao encontrado')
    return item


@router.post('/', response_model=ConsultaResponse, status_code=201)
def criar(item: ConsultaCreate, db: Session = Depends(get_db)):
    return crud.create_consulta(db, item)


@router.put('/{item_id}', response_model=ConsultaResponse)
def atualizar(item_id: int, item: ConsultaUpdate, db: Session = Depends(get_db)):
    updated = crud.update_consulta(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail='Nao encontrado')
    return updated


@router.delete('/{item_id}', status_code=204)
def deletar(item_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_consulta(db, item_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Nao encontrado')