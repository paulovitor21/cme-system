from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.user_routes import router as user_router
from app.routes.material_routes import router as material_router
from app.routes.process_routes import router as process_router

from app.models.user import Base
from app.models import user, material, process
from app.database import engine

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(
    title="CME API",
    description="API para Sistema de Central de Materiais e Esterilização",
    version="1.0.0"
)

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Frontend React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(user_router)
app.include_router(material_router)
app.include_router(process_router)

@app.get("/", tags=["root"])
async def root():
    return {"message": "Bem-vindo à API do Sistema CME"}