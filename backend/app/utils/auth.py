from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.database import get_db_session
from app.repositories.user_repository import UserRepository
from app.models.user import UserRole
import os

# Configurações
SECRET_KEY = os.getenv("SECRET_KEY", "chave_fallback")
ALGORITHM = "HS256"

# Token OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

# Instanciar repositório
user_repo = UserRepository()

# Obter usuário atual a partir do token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db_session)):
    print("TOKEN RECEBIDO:", token)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou usuário não autenticado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        print("USER ID EXTRAÍDO DO TOKEN:", user_id)
        if user_id is None:
            raise credentials_exception
    except JWTError as e:
        print("JWT ERROR:", str(e))
        raise credentials_exception

    user = user_repo.get_user_by_id(db, user_id)
    if user is None:
        print("USUÁRIO NÃO ENCONTRADO")
        raise credentials_exception

    print("USUÁRIO ENCONTRADO:", user.email, "-", user.role)

    # Converter string para enum
    if isinstance(user.role, str):
        try:
            user.role = UserRole(user.role)
        except ValueError:
            print("ERRO: valor de role inválido:", user.role)
            raise credentials_exception

    return user

# Dependência para ADMIN
def is_admin(user=Depends(get_current_user)):
    if user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Acesso restrito ao usuário ADMIN")
    return user

# Dependência para ENFERMAGEM
def is_nurse(user=Depends(get_current_user)):
    if user.role != UserRole.NURSE:
        raise HTTPException(status_code=403, detail="Acesso restrito ao usuário ENFERMAGEM")
    return user

# Dependência para TÉCNICO
def is_technician(user=Depends(get_current_user)):
    if user.role != UserRole.TECHNICIAN:
        raise HTTPException(status_code=403, detail="Acesso restrito ao usuário TÉCNICO")
    return user

# Função genérica para múltiplos papéis
def role_required(allowed_roles: list[UserRole]):
    def wrapper(current_user=Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permissão insuficiente"
            )
        return current_user
    return wrapper
