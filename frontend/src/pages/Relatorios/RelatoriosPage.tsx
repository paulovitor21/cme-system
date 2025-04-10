// src/pages/Relatorios/RelatoriosPage.tsx
import { useNavigate } from "react-router-dom";

const apiUrl = "http://localhost:8000/api";

export default function RelatoriosPage() {
  const navigate = useNavigate();

  const gerarRelatorio = async (formato: "pdf" | "xlsx") => {
    try {
      const token = localStorage.getItem("token");
      const response = await fetch(`${apiUrl}/processos/relatorio/${formato}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error("Erro ao gerar relatório");
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `relatorio_processos.${formato}`;
      a.click();
    } catch (err) {
      alert("Erro ao baixar o relatório.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow">
        <h2 className="mb-3">Relatórios</h2>
        <p>Baixe os relatórios dos processos realizados:</p>

        <div className="d-flex gap-3 mt-4">
          <button className="btn btn-danger" onClick={() => gerarRelatorio("pdf")}>
            Baixar PDF
          </button>
          <button className="btn btn-success" onClick={() => gerarRelatorio("xlsx")}>
            Baixar XLSX
          </button>
        </div>
      </div>
    </div>
  );
}
