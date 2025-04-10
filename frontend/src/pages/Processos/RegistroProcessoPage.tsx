import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const apiUrl = "http://localhost:8000/api";

export default function RegistroProcessoPage() {
  const navigate = useNavigate();

  const [serial, setSerial] = useState("");
  const [etapa, setEtapa] = useState("recebimento");
  const [status, setStatus] = useState("concluido");
  const [descricaoFalha, setDescricaoFalha] = useState("");
  const [mensagem, setMensagem] = useState("");

  useEffect(() => {
    const role = localStorage.getItem("role");
    if (role !== "tecnico") {
      navigate("/dashboard");
    }
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setMensagem("");

    try {
      const token = localStorage.getItem("token");
      const payload = {
        serial,
        etapa,
        status,
        descricao_falha: status === "falha" ? descricaoFalha : null,
      };

      await axios.post(`${apiUrl}/processos/`, payload, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setMensagem("Etapa registrada com sucesso!");
      setSerial("");
      setEtapa("recebimento");
      setStatus("concluido");
      setDescricaoFalha("");
    } catch (err: any) {
      setMensagem("Erro ao registrar etapa.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="mb-4">Registrar Etapa do Processo</h2>

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Serial do Material:</label>
            <input
              type="text"
              className="form-control"
              value={serial}
              onChange={(e) => setSerial(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Etapa:</label>
            <select
              className="form-select"
              value={etapa}
              onChange={(e) => setEtapa(e.target.value)}
            >
              <option value="recebimento">Recebimento</option>
              <option value="lavagem">Lavagem</option>
              <option value="esterilizacao">Esterilização</option>
              <option value="distribuicao">Distribuição</option>
            </select>
          </div>

          <div className="mb-3">
            <label className="form-label">Status:</label>
            <select
              className="form-select"
              value={status}
              onChange={(e) => setStatus(e.target.value)}
            >
              <option value="concluido">Concluído</option>
              <option value="falha">Falha</option>
            </select>
          </div>

          {status === "falha" && (
            <div className="mb-3">
              <label className="form-label">Descrição da Falha:</label>
              <textarea
                className="form-control"
                value={descricaoFalha}
                onChange={(e) => setDescricaoFalha(e.target.value)}
              />
            </div>
          )}

          <button type="submit" className="btn btn-primary w-100">
            Registrar
          </button>
        </form>

        {mensagem && (
          <div className="alert alert-info mt-3 text-center">{mensagem}</div>
        )}
      </div>
    </div>
  );
}
