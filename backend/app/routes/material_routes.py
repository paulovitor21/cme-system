from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models.material import MaterialCreate, MaterialResponse
from app.repositories.material_repository import MaterialRepository
from app.database import get_db_session
from app.models.user import User, UserRole
from app.routes.user_routes import get_current_user
from app.utils.auth import role_required

router = APIRouter(
    prefix="/api/materiais",
    tags=["materiais"]
)

material_repo = MaterialRepository()

# Criar novo material (apenas técnicos podem cadastrar)
@router.post("/", response_model=MaterialResponse, status_code=status.HTTP_201_CREATED)
def create_material(
    material_data: MaterialCreate,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(role_required([UserRole.TECHNICIAN]))
):
    return material_repo.create_material(db, material_data)

# Listar todos os materiais (enfermagem e administrativo podem consultar)
@router.get("/", response_model=List[MaterialResponse])
def list_materiais(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(role_required([UserRole.NURSE, UserRole.ADMIN]))
):
    return material_repo.get_all(db, skip, limit)

# Buscar material por serial
@router.get("/{serial}", response_model=MaterialResponse)
def get_material_by_serial(
    serial: str,
    db: Session = Depends(get_db_session),
    current_user: User = Depends(role_required([UserRole.NURSE, UserRole.ADMIN]))
):
    material = material_repo.get_by_serial(db, serial)
    if not material:
        raise HTTPException(status_code=404, detail="Material não encontrado")
    return material
