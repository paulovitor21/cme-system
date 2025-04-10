import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();
  const [name, setName] = useState<string | null>(null);
  const [role, setRole] = useState<string | null>(null);
  const [email, setEmail] = useState<string | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    const storedRole = localStorage.getItem("role");
    const storedEmail = localStorage.getItem("email");
    const storedName = localStorage.getItem("name");

    if (!token) {
      navigate("/login");
    }

    setRole(storedRole);
    setEmail(storedEmail);
    setName(storedName);
  }, []);

  const handleLogout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <div className="container mt-5">
      <div className="card p-4 shadow">
        <h2 className="mb-4">Bem-vindo ao Sistema CME</h2>

        <p><strong>Usuário:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>Função:</strong> {role}</p>

        <div className="row mt-4">
          {role === "administrativo" && (
            <div className="col-12">
              <button
                className="btn btn-primary w-100 mb-3"
                onClick={() => navigate("/usuarios")}
              >
                Gerenciar Usuários
              </button>
            </div>
          )}

          {role === "tecnico" && (
            <>
              <div className="col-md-6 mb-3">
                <button
                  className="btn btn-success w-100"
                  onClick={() => navigate("/processos")}
                >
                  Registrar Processo
                </button>
              </div>
              <div className="col-md-6 mb-3">
                <button
                  className="btn btn-info w-100"
                  onClick={() => navigate("/materiais")}
                >
                  Cadastrar Materiais
                </button>
              </div>
            </>
          )}

          {role === "enfermagem" && (
            <>
              <div className="col-md-6 mb-3">
                <button
                  className="btn btn-warning w-100"
                  onClick={() => navigate("/rastreabilidade")}
                >
                  Consultar Rastreabilidade
                </button>
              </div>
              <div className="col-md-6 mb-3">
                <button
                  className="btn btn-secondary w-100"
                  onClick={() => navigate("/relatorios")}
                >
                  Gerar Relatórios
                </button>
              </div>
            </>
          )}
        </div>

        <button
          className="btn btn-danger mt-4"
          onClick={handleLogout}
        >
          Sair
        </button>
      </div>
    </div>
  );
}
