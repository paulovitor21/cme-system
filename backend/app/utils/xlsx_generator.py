# app/utils/xlsx_generator.py

from openpyxl import Workbook
from openpyxl.styles import Font
from io import BytesIO
from typing import List
from app.models.process import Processo

def generate_xlsx_report(processos: List[Processo]) -> BytesIO:
    wb = Workbook()
    ws = wb.active
    ws.title = "Relatório de Processos"

    # Cabeçalho
    headers = ["Serial", "Etapa", "Status", "Descrição da Falha", "Usuário", "Data/Hora"]
    ws.append(headers)

    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Conteúdo
    for p in processos:
        ws.append([
            p.serial,
            p.etapa.value,
            p.status.value,
            p.descricao_falha or "-",
            p.nome_usuario,
            p.data_hora.strftime("%d/%m/%Y %H:%M")
        ])

    # Salvar em memória
    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)
    return file_stream
