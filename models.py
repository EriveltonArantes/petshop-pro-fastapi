from sqlalchemy import Column, Integer, BigInteger, String, Float, Boolean, Date, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    nome = Column(String(255), nullable=False)
    especie = Column(String(255))
    raca = Column(String(255))
    peso = Column(Float, nullable=False)


class Dono(Base):
    __tablename__ = "donos"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    cpf = Column(String(255), nullable=False, unique=True)
    telefone = Column(String(255), nullable=False)


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    pet_id = Column(Integer, ForeignKey('pets.id'), index=True)
    dono_id = Column(Integer, ForeignKey('donos.id'), index=True)
    data = Column(DateTime)
    diagnostico = Column(Text, nullable=False)
    status = Column(String(255), nullable=False)
    observacoes = Column(Text)


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    nome = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoria = Column(String(255), nullable=False)

