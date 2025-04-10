from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from typing import List
from app.models.process import Processo
from textwrap import wrap

def generate_pdf_report(processos: List[dict]) -> BytesIO:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4
    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, y, "Relatório de Processos")
    y -= 40

    headers = ["Serial", "Etapa", "Status", "Falha", "Usuário", "Data/Hora"]
    x_positions = [40, 140, 220, 300, 400, 500]

    def draw_headers():
        pdf.setFont("Helvetica-Bold", 10)
        for i, header in enumerate(headers):
            pdf.drawString(x_positions[i], y, header)

    draw_headers()
    y -= 20
    pdf.setFont("Helvetica", 9)

    for proc in processos:
        # Quebrar colunas com conteúdo maior
        serial_lines = wrap(proc["serial"], width=20)
        falha_lines = wrap(proc.get("descricao_falha") or "-", width=25)
        nome_usuario_lines = wrap(proc["nome_usuario"], width=20)
        data_hora_str = str(proc["data_hora"])

        max_lines = max(len(serial_lines), len(falha_lines), len(nome_usuario_lines))

        if y - (max_lines * 15) < 60:
            pdf.showPage()
            y = height - 50
            draw_headers()
            y -= 20
            pdf.setFont("Helvetica", 9)

        for i in range(max_lines):
            pdf.drawString(x_positions[0], y, serial_lines[i] if i < len(serial_lines) else "")
            pdf.drawString(x_positions[1], y, str(proc["etapa"]) if i == 0 else "")
            pdf.drawString(x_positions[2], y, str(proc["status"]) if i == 0 else "")
            pdf.drawString(x_positions[3], y, falha_lines[i] if i < len(falha_lines) else "")
            pdf.drawString(x_positions[4], y, nome_usuario_lines[i] if i < len(nome_usuario_lines) else "")
            pdf.drawString(x_positions[5], y, data_hora_str if i == 0 else "")
            y -= 15

    pdf.save()
    buffer.seek(0)
    return buffer
