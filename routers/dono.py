from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
import crud
from schemas import DonoCreate, DonoUpdate, DonoResponse

router = APIRouter(prefix="/api/donos", tags=["donos"])


@router.get('/', response_model=List[DonoResponse])
def listar(skip: int = 0, limit: int = 100, nome: Optional[str] = None, db: Session = Depends(get_db)):
    items = crud.get_all_dono(db, skip=skip, limit=limit)
    if nome:
        items = [i for i in items if i.nome and nome.lower() in i.nome.lower()]
    return items


@router.get('/{item_id}', response_model=DonoResponse)
def buscar(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_dono(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Nao encontrado')
    return item


@router.post('/', response_model=DonoResponse, status_code=201)
def criar(item: DonoCreate, db: Session = Depends(get_db)):
    if getattr(item, 'email', None) and crud.exists_dono_by_email(db, item.email):
        raise HTTPException(status_code=409, detail='Email ja cadastrado')
    if getattr(item, 'cpf', None) and crud.exists_dono_by_cpf(db, item.cpf):
        raise HTTPException(status_code=409, detail='Cpf ja cadastrado')
    return crud.create_dono(db, item)


@router.put('/{item_id}', response_model=DonoResponse)
def atualizar(item_id: int, item: DonoUpdate, db: Session = Depends(get_db)):
    if getattr(item, 'email', None) and crud.exists_dono_by_email(db, item.email, exclude_id=item_id):
        raise HTTPException(status_code=409, detail='Email ja cadastrado')
    if getattr(item, 'cpf', None) and crud.exists_dono_by_cpf(db, item.cpf, exclude_id=item_id):
        raise HTTPException(status_code=409, detail='Cpf ja cadastrado')
    updated = crud.update_dono(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail='Nao encontrado')
    return updated


@router.delete('/{item_id}', status_code=204)
def deletar(item_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_dono(db, item_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Nao encontrado')