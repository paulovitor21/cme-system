from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User, UserCreate, UserUpdate
from typing import List, Optional

class UserRepository:
    def create_user(self, db: Session, user_data: UserCreate) -> User:
        """Criar um novo usuário"""
        db_user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=User.get_password_hash(user_data.password),
            role=user_data.role
        )
        
        try:
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise ValueError("Email já cadastrado")
    
    def get_user_by_id(self, db: Session, user_id: str) -> Optional[User]:
        """Buscar usuário pelo ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        """Buscar usuário pelo email"""
        return db.query(User).filter(User.email == email).first()
    
    def get_all_users(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """Buscar todos os usuários com paginação"""
        return db.query(User).offset(skip).limit(limit).all()
    
    def update_user(self, db: Session, user_id: str, user_data: UserUpdate) -> Optional[User]:
        """Atualizar dados do usuário"""
        db_user = self.get_user_by_id(db, user_id)
        if not db_user:
            return None
            
        # Atualiza apenas os campos fornecidos
        update_data = user_data.dict(exclude_unset=True)
        
        # Se houver uma senha nova, faz o hash
        if "password" in update_data:
            update_data["password_hash"] = User.get_password_hash(update_data.pop("password"))
            
        for key, value in update_data.items():
            setattr(db_user, key, value)
            
        try:
            db.commit()
            db.refresh(db_user)
            return db_user
        except IntegrityError:
            db.rollback()
            raise ValueError("Email já cadastrado")
    
    def delete_user(self, db: Session, user_id: str) -> bool:
        """Deletar um usuário pelo ID"""
        db_user = self.get_user_by_id(db, user_id)
        if not db_user:
            return False
            
        db.delete(db_user)
        db.commit()
        return True
    
    def authenticate_user(self, db: Session, email: str, password: str) -> Optional[User]:
        """Autenticar um usuário pelo email e senha"""
        user = self.get_user_by_email(db, email)
        if not user or not user.verify_password(password):
            return None
        return user