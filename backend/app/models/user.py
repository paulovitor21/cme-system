from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime
import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from passlib.context import CryptContext
from app.models import Base

# Configuração do bcrypt para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRole(str, Enum):
    ADMIN = "administrativo"
    NURSE = "enfermagem"
    TECHNICIAN = "tecnico"

# Modelo SQLAlchemy para o banco de dados
class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
    
    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

# Schemas Pydantic para validação de dados e serialização
class UserBase(BaseModel):
    name: str
    email: EmailStr
    
class UserCreate(UserBase):
    password: str
    role: UserRole
    
    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Senha deve ter pelo menos 8 caracteres')
        return v

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    
class UserResponse(UserBase):
    id: str
    role: UserRole
    is_active: bool
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str