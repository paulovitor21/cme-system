import { useState } from "react";
import axios from "axios";

const apiUrl = "http://localhost:8000/api";

export default function RastreabilidadePage() {
  const [serial, setSerial] = useState("");
  const [processos, setProcessos] = useState([]);
  const [mensagem, setMensagem] = useState("");

  const buscar = async () => {
    setMensagem("");
    setProcessos([]);

    const token = localStorage.getItem("token");
    const role = localStorage.getItem("role");

    if (role !== "enfermagem") {
      setMensagem("Acesso restrito.");
      return;
    }

    try {
      const res = await axios.get(`${apiUrl}/processos/${serial}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setProcessos(res.data);
    } catch (err: any) {
      setMensagem("Nenhum processo encontrado ou erro na requisição.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow">
        <h2 className="mb-4">Consultar Rastreabilidade</h2>

        <div className="mb-3 row">
          <div className="col-md-8">
            <input
              type="text"
              className="form-control"
              placeholder="Digite o serial do material"
              value={serial}
              onChange={(e) => setSerial(e.target.value)}
            />
          </div>
          <div className="col-md-4">
            <button className="btn btn-primary w-100" onClick={buscar}>
              Buscar
            </button>
          </div>
        </div>

        {mensagem && <div className="alert alert-info">{mensagem}</div>}

        {processos.length > 0 && (
          <div className="table-responsive mt-4">
            <table className="table table-bordered table-hover">
              <thead className="table-light">
                <tr>
                  <th>Etapa</th>
                  <th>Status</th>
                  <th>Falha</th>
                  <th>Data/Hora</th>
                </tr>
              </thead>
              <tbody>
                {processos.map((p: any) => (
                  <tr key={p.id}>
                    <td>{p.etapa}</td>
                    <td>{p.status}</td>
                    <td>{p.descricao_falha || "-"}</td>
                    <td>{new Date(p.data_hora).toLocaleString()}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
