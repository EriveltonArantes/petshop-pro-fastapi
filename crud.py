from sqlalchemy.orm import Session
from typing import Optional, List
from models import Pet, Dono, Consulta, Produto
from schemas import PetCreate, PetUpdate, DonoCreate, DonoUpdate, ConsultaCreate, ConsultaUpdate, ProdutoCreate, ProdutoUpdate


def get_all_pet(db: Session, skip: int = 0, limit: int = 100) -> List[Pet]:
    return db.query(Pet).offset(skip).limit(limit).all()

def get_pet(db: Session, item_id: int) -> Optional[Pet]:
    return db.query(Pet).filter(Pet.id == item_id).first()

def create_pet(db: Session, item: PetCreate) -> Pet:
    db_item = Pet(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_pet(db: Session, item_id: int, item: PetUpdate) -> Optional[Pet]:
    db_item = get_pet(db, item_id)
    if not db_item:
        return None
    for k, v in item.model_dump(exclude_unset=True).items():
        if k not in ('created_at', 'updated_at'):
            setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_pet(db: Session, item_id: int) -> bool:
    db_item = get_pet(db, item_id)
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True


def get_all_dono(db: Session, skip: int = 0, limit: int = 100) -> List[Dono]:
    return db.query(Dono).offset(skip).limit(limit).all()

def get_dono(db: Session, item_id: int) -> Optional[Dono]:
    return db.query(Dono).filter(Dono.id == item_id).first()

def exists_dono_by_email(db: Session, email: str, exclude_id: int = 0) -> bool:
    q = db.query(Dono).filter(Dono.email == email)
    if exclude_id:
        q = q.filter(Dono.id != exclude_id)
    return q.first() is not None

def exists_dono_by_cpf(db: Session, cpf: str, exclude_id: int = 0) -> bool:
    q = db.query(Dono).filter(Dono.cpf == cpf)
    if exclude_id:
        q = q.filter(Dono.id != exclude_id)
    return q.first() is not None

def create_dono(db: Session, item: DonoCreate) -> Dono:
    db_item = Dono(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_dono(db: Session, item_id: int, item: DonoUpdate) -> Optional[Dono]:
    db_item = get_dono(db, item_id)
    if not db_item:
        return None
    for k, v in item.model_dump(exclude_unset=True).items():
        if k not in ('created_at', 'updated_at'):
            setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_dono(db: Session, item_id: int) -> bool:
    db_item = get_dono(db, item_id)
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True


def get_all_consulta(db: Session, skip: int = 0, limit: int = 100) -> List[Consulta]:
    return db.query(Consulta).offset(skip).limit(limit).all()

def get_consulta(db: Session, item_id: int) -> Optional[Consulta]:
    return db.query(Consulta).filter(Consulta.id == item_id).first()

def create_consulta(db: Session, item: ConsultaCreate) -> Consulta:
    db_item = Consulta(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_consulta(db: Session, item_id: int, item: ConsultaUpdate) -> Optional[Consulta]:
    db_item = get_consulta(db, item_id)
    if not db_item:
        return None
    for k, v in item.model_dump(exclude_unset=True).items():
        if k not in ('created_at', 'updated_at'):
            setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_consulta(db: Session, item_id: int) -> bool:
    db_item = get_consulta(db, item_id)
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True


def get_all_produto(db: Session, skip: int = 0, limit: int = 100) -> List[Produto]:
    return db.query(Produto).offset(skip).limit(limit).all()

def get_produto(db: Session, item_id: int) -> Optional[Produto]:
    return db.query(Produto).filter(Produto.id == item_id).first()

def create_produto(db: Session, item: ProdutoCreate) -> Produto:
    db_item = Produto(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_produto(db: Session, item_id: int, item: ProdutoUpdate) -> Optional[Produto]:
    db_item = get_produto(db, item_id)
    if not db_item:
        return None
    for k, v in item.model_dump(exclude_unset=True).items():
        if k not in ('created_at', 'updated_at'):
            setattr(db_item, k, v)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_produto(db: Session, item_id: int) -> bool:
    db_item = get_produto(db, item_id)
    if not db_item:
        return False
    db.delete(db_item)
    db.commit()
    return True

