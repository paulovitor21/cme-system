from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.models.process import ProcessoCreate, ProcessoResponse
from app.repositories.process_repository import ProcessoRepository
from app.repositories.material_repository import MaterialRepository  # Novo

from fastapi.responses import StreamingResponse
from app.utils.xlsx_generator import generate_xlsx_report

from app.database import get_db_session
from app.utils.auth import is_nurse, is_technician, get_current_user

router = APIRouter(
    prefix="/api/processos",
    tags=["rastreabilidade"]
)

repo = ProcessoRepository()
material_repo = MaterialRepository()  # Novo

# Registrar etapa - Apenas técnico
@router.post("/", response_model=ProcessoResponse, status_code=status.HTTP_201_CREATED)
def registrar_processo(
    processo_data: ProcessoCreate,
    db: Session = Depends(get_db_session),
    current_user = Depends(is_technician)
):
    # Verificar se o serial existe na tabela de materiais
    material = material_repo.get_by_serial(db, processo_data.serial)
    if not material:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material com esse serial não encontrado"
        )

    try:
        return repo.registrar_etapa(db, processo_data, usuario_id=current_user.id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# Listar todos os processos - Enfermagem/Admin
@router.get("/", response_model=List[ProcessoResponse])
def listar_processos(
    db: Session = Depends(get_db_session),
    current_user = Depends(is_nurse)
):
    return repo.listar_todos(db)

# Ver processos por serial - Enfermagem/Admin
@router.get("/{serial}", response_model=List[ProcessoResponse])
def listar_por_serial(
    serial: str,
    db: Session = Depends(get_db_session),
    current_user = Depends(is_nurse)
):
    processos = repo.listar_por_serial(db, serial)
    if not processos:
        raise HTTPException(status_code=404, detail="Serial não encontrado")
    return processos

# Quantidade de ciclos por serial - Enfermagem/Admin
@router.get("/{serial}/ciclos")
def contar_ciclos(
    serial: str,
    db: Session = Depends(get_db_session),
    current_user = Depends(is_nurse)
):
    return {"serial": serial, "ciclos_completos": repo.contar_ciclos(db, serial)}

#  listagem de falhas por serial - Enfermagem
@router.get("/{serial}/falhas", response_model=List[ProcessoResponse])
def listar_falhas_serial(
    serial: str,
    db: Session = Depends(get_db_session),
    current_user = Depends(is_nurse)
):
    falhas = repo.listar_falhas_por_serial(db, serial)
    if not falhas:
        raise HTTPException(status_code=404, detail="Nenhuma falha encontrada para este serial")
    return falhas

# Gerar relatório XLSX - Enfermagem/Admin
@router.get("/relatorio/xlsx")
def gerar_relatorio_xlsx(
    db: Session = Depends(get_db_session),
    current_user = Depends(is_nurse)
):
    resultados = repo.listar_todos_com_usuario(db)

    # Adiciona dinamicamente o nome do usuário ao modelo Processo
    processos_formatados = []
    for processo, nome_usuario in resultados:
        processo.nome_usuario = nome_usuario
        processos_formatados.append(processo)

    arquivo = generate_xlsx_report(processos_formatados)

    return StreamingResponse(
        arquivo,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=relatorio_processos.xlsx"}
    )

# Gerar relatório PDF - Enfermagem/Admin
@router.get("/relatorio/pdf")
def gerar_relatorio_pdf(
    db: Session = Depends(get_db_session),
    current_user = Depends(is_nurse)
):
    processos = repo.listar_todos_com_usuario(db)
    
    # Mapear os dados
    dados_formatados = [{
        "serial": p.serial,
        "etapa": p.etapa.value,
        "status": p.status.value,
        "descricao_falha": p.descricao_falha,
        "nome_usuario": nome,
        "data_hora": p.data_hora.strftime("%d/%m/%Y %H:%M")
    } for p, nome in processos]

    from app.utils.pdf_generator import generate_pdf_report
    pdf_stream = generate_pdf_report(dados_formatados)

    return StreamingResponse(
        pdf_stream,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=relatorio_processos.pdf"}
    )








