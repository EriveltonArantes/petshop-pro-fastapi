from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
import crud
from schemas import PetCreate, PetUpdate, PetResponse

router = APIRouter(prefix="/api/pets", tags=["pets"])


@router.get('/', response_model=List[PetResponse])
def listar(skip: int = 0, limit: int = 100, nome: Optional[str] = None, db: Session = Depends(get_db)):
    items = crud.get_all_pet(db, skip=skip, limit=limit)
    if nome:
        items = [i for i in items if i.nome and nome.lower() in i.nome.lower()]
    return items


@router.get('/{item_id}', response_model=PetResponse)
def buscar(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_pet(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail='Nao encontrado')
    return item


@router.post('/', response_model=PetResponse, status_code=201)
def criar(item: PetCreate, db: Session = Depends(get_db)):
    return crud.create_pet(db, item)


@router.put('/{item_id}', response_model=PetResponse)
def atualizar(item_id: int, item: PetUpdate, db: Session = Depends(get_db)):
    updated = crud.update_pet(db, item_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail='Nao encontrado')
    return updated


@router.delete('/{item_id}', status_code=204)
def deletar(item_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_pet(db, item_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Nao encontrado')