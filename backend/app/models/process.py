# app/models/process.py
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from uuid import uuid4
from enum import Enum as PyEnum
from pydantic import BaseModel, Field
from typing import Optional
from app.models import Base

# Enum com as etapas do processo
class EtapaEnum(str, PyEnum):
    RECEBIMENTO = "recebimento"
    LAVAGEM = "lavagem"
    ESTERILIZACAO = "esterilizacao"
    DISTRIBUICAO = "distribuicao"

# Enum para status
class StatusEnum(str, PyEnum):
    CONCLUIDO = "concluido"
    FALHA = "falha"

# Modelo SQLAlchemy
class Processo(Base):
    __tablename__ = "processos"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    serial = Column(String, nullable=False, index=True)
    etapa = Column(Enum(EtapaEnum), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    descricao_falha = Column(String, nullable=True)
    usuario_id = Column(String, ForeignKey("users.id"), nullable=False)
    data_hora = Column(DateTime, default=datetime.utcnow)

# Schemas Pydantic
class ProcessoBase(BaseModel):
    serial: str
    etapa: EtapaEnum
    status: StatusEnum
    descricao_falha: Optional[str] = None

class ProcessoCreate(ProcessoBase):
    pass

class ProcessoResponse(ProcessoBase):
    id: str
    usuario_id: str
    data_hora: datetime

    class Config:
        orm_mode = True
