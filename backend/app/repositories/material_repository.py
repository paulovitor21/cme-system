from sqlalchemy.orm import Session
from app.models.material import Material, MaterialCreate
from app.utils.gerador_serial import gerar_serial
from uuid import uuid4
from datetime import datetime

class MaterialRepository:
    # def generate_serial(self, nome: str) -> str:
    #     # Gera um serial único baseado no nome + UUID simples
    #     base = nome.replace(" ", "-").upper()
    #     unique = uuid4().hex[:6].upper()
    #     return f"{base}-{unique}"

    def create_material(self, db: Session, material_data: MaterialCreate) -> Material:
        #serial = self.generate_serial(material_data.nome)
        serial = gerar_serial(material_data.nome)


        new_material = Material(
            nome=material_data.nome,
            tipo=material_data.tipo,
            data_validade=material_data.data_validade,
            serial=serial,
            created_at=datetime.utcnow()
        )

        db.add(new_material)
        db.commit()
        db.refresh(new_material)
        return new_material

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Material).offset(skip).limit(limit).all()

    def get_by_serial(self, db: Session, serial: str):
        return db.query(Material).filter(Material.serial == serial).first()

    def get_by_id(self, db: Session, material_id: str):
        return db.query(Material).filter(Material.id == material_id).first()
