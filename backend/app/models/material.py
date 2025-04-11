from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date
from uuid import uuid4
from pydantic import BaseModel, Field
from typing import Optional
from app.models import Base

# Modelo SQLAlchemy
class Material(Base):
    __tablename__ = "materiais"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    data_validade = Column(Date, nullable=False)
    serial = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Schemas Pydantic
class MaterialBase(BaseModel):
    nome: str
    tipo: str
    data_validade: date

class MaterialCreate(MaterialBase):
    pass

class MaterialResponse(MaterialBase):
    id: str
    serial: str
    created_at: datetime

    class Config:
        orm_mode = True
