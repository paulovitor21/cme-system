# Coloque este arquivo em backend/scripts/create_admin.py

from sqlalchemy.orm import Session
from app.models.user import User, UserRole
from app.database import engine, SessionLocal
import uuid

def create_admin_user():
    """Cria um usuário administrador inicial se não existir nenhum"""
    db = SessionLocal()
    
    # Verificar se já existe algum usuário admin
    admin = db.query(User).filter(User.role == UserRole.ADMIN).first()
    
    if not admin:
        # Criar usuário admin
        admin_user = User(
            id=str(uuid.uuid4()),
            name="Admin",
            email="admin@cme.com",
            password_hash=User.get_password_hash("admin123"),
            role=UserRole.ADMIN
        )
        
        db.add(admin_user)
        db.commit()
        print("Usuário administrador criado com sucesso!")
        print("Email: admin@cme.com")
        print("Senha: admin123")
    else:
        print("Usuário administrador já existe.")
    
    db.close()

if __name__ == "__main__":
    create_admin_user()