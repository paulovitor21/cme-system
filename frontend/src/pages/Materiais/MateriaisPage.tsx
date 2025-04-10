import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const apiUrl = "http://localhost:8000/api";

export default function MateriaisPage() {
  const navigate = useNavigate();

  const [nome, setNome] = useState("");
  const [tipo, setTipo] = useState("");
  const [validade, setValidade] = useState("");
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

      await axios.post(`${apiUrl}/materiais/`, {
        nome,
        tipo,
        data_validade: validade,
      }, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setMensagem("Material cadastrado com sucesso!");
      setNome("");
      setTipo("");
      setValidade("");
    } catch (error) {
      setMensagem("Erro ao cadastrar material.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow">
        <h2 className="mb-4">Cadastro de Materiais</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Nome</label>
            <input
              type="text"
              className="form-control"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Tipo</label>
            <input
              type="text"
              className="form-control"
              value={tipo}
              onChange={(e) => setTipo(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Data de Validade</label>
            <input
              type="date"
              className="form-control"
              value={validade}
              onChange={(e) => setValidade(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn btn-success w-100">Cadastrar</button>
        </form>

        {mensagem && (
          <div className="alert alert-info mt-3 text-center">
            {mensagem}
          </div>
        )}
      </div>
    </div>
  );
}
