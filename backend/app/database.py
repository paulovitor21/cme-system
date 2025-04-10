import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import urllib.parse  # Adicione esta linha

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do banco de dados
# POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
# POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "@manaus")
# POSTGRES_HOST = os.getenv("POSTGRES_HOST", "db")
# POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
# POSTGRES_DB = os.getenv("POSTGRES_DB", "cme_db")

# Codificar a senha para lidar com caracteres especiais
#encoded_password = urllib.parse.quote_plus(POSTGRES_PASSWORD)

# Criar URL de conexão com a senha codificada
#DATABASE_URL = f"postgresql://{POSTGRES_USER}:{encoded_password}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:%40manaus@db:5432/cme_db")
# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Criar fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão do banco de dados
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()