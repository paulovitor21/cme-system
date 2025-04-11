from app.models.process import Processo
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.process import ProcessoCreate
from app.models.process import StatusEnum

from datetime import datetime

class ProcessoRepository:

    def registrar_etapa(self, db: Session, dados: ProcessoCreate, usuario_id: str) -> Processo:
        # Verificar duplicidade da etapa
        etapa_existente = db.query(Processo).filter_by(
            serial=dados.serial,
            etapa=dados.etapa
        ).first()

        if etapa_existente:
            raise ValueError(f"A etapa '{dados.etapa}' já foi registrada para o serial '{dados.serial}'.")

        novo_processo = Processo(
            serial=dados.serial,
            etapa=dados.etapa,
            status=dados.status,
            descricao_falha=dados.descricao_falha,
            usuario_id=usuario_id,
            data_hora=datetime.utcnow()
        )

        db.add(novo_processo)
        db.commit()
        db.refresh(novo_processo)
        return novo_processo

    def listar_todos(self, db: Session):
        return db.query(Processo).order_by(Processo.data_hora.desc()).all()

    def listar_por_serial(self, db: Session, serial: str):
        return db.query(Processo).filter(Processo.serial == serial).order_by(Processo.data_hora).all()

    def contar_ciclos(self, db: Session, serial: str):
        # Considera 4 etapas concluídas como 1 ciclo
        etapas_concluidas = db.query(Processo).filter_by(
            serial=serial,
            status="concluido"
        ).count()
        return etapas_concluidas // 4
    
    def listar_falhas_por_serial(self, db: Session, serial: str):
        return db.query(Processo).filter(
            Processo.serial == serial,
            Processo.status == StatusEnum.FALHA
        ).all()
    
    def listar_todos_com_usuario(self, db: Session):
        return (
            db.query(Processo, User.name)
            .join(User, Processo.usuario_id == User.id)
            .order_by(Processo.data_hora.desc())
            .all()
        )
    def listar_por_usuario(self, db: Session, usuario_id: str):
        return (
            db.query(Processo)
            .filter(Processo.usuario_id == usuario_id)
            .order_by(Processo.data_hora.desc())
        .all()
        )
            


