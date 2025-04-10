// src/pages/Usuarios/UsuariosPage.tsx
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const apiUrl = "http://localhost:8000/api";

export default function UsuariosPage() {
  const [usuarios, setUsuarios] = useState([]);
  const [mensagem, setMensagem] = useState("");
  const [novoUsuario, setNovoUsuario] = useState({
    name: "",
    email: "",
    password: "",
    role: "tecnico",
  });

  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  useEffect(() => {
    const role = localStorage.getItem("role");
    if (role !== "administrativo") {
      navigate("/dashboard");
      return;
    }

    carregarUsuarios();
  }, []);

  const carregarUsuarios = () => {
    axios.get(`${apiUrl}/users/`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(res => setUsuarios(res.data))
    .catch(() => alert("Erro ao carregar usuários"));
  };

  const handleCadastro = (e: React.FormEvent) => {
    e.preventDefault();
    setMensagem("");

    axios.post(`${apiUrl}/users/`, novoUsuario, {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(() => {
      setMensagem("Usuário cadastrado com sucesso!");
      setNovoUsuario({ name: "", email: "", password: "", role: "tecnico" });
      carregarUsuarios();
    })
    .catch(() => setMensagem("Erro ao cadastrar usuário"));
  };

  const excluirUsuario = (id: string) => {
    if (confirm("Tem certeza que deseja excluir este usuário?")) {
      axios.delete(`${apiUrl}/users/${id}`, {
        headers: { Authorization: `Bearer ${token}` }
      })
      .then(() => carregarUsuarios())
      .catch(() => alert("Erro ao excluir usuário"));
    }
  };

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Gerenciar Usuários</h2>

      <div className="card mb-4 p-4 shadow-sm">
        <h4 className="mb-3">Cadastrar Novo Usuário</h4>
        <form onSubmit={handleCadastro} className="row g-3">
          <div className="col-md-6">
            <input
              type="text"
              className="form-control"
              placeholder="Nome"
              value={novoUsuario.name}
              onChange={e => setNovoUsuario({ ...novoUsuario, name: e.target.value })}
              required
            />
          </div>
          <div className="col-md-6">
            <input
              type="email"
              className="form-control"
              placeholder="Email"
              value={novoUsuario.email}
              onChange={e => setNovoUsuario({ ...novoUsuario, email: e.target.value })}
              required
            />
          </div>
          <div className="col-md-6">
            <input
              type="password"
              className="form-control"
              placeholder="Senha"
              value={novoUsuario.password}
              onChange={e => setNovoUsuario({ ...novoUsuario, password: e.target.value })}
              required
            />
          </div>
          <div className="col-md-4">
            <select
              className="form-select"
              value={novoUsuario.role}
              onChange={e => setNovoUsuario({ ...novoUsuario, role: e.target.value })}
            >
              <option value="administrativo">Administrativo</option>
              <option value="tecnico">Técnico</option>
              <option value="enfermagem">Enfermagem</option>
            </select>
          </div>
          <div className="col-md-2 d-grid">
            <button type="submit" className="btn btn-primary">Cadastrar</button>
          </div>
        </form>
        {mensagem && <p className="mt-3 text-success">{mensagem}</p>}
      </div>

      <div className="card p-4 shadow-sm">
        <h4 className="mb-3">Lista de Usuários</h4>
        <div className="table-responsive">
          <table className="table table-bordered table-hover">
            <thead className="table-light">
              <tr>
                <th>Nome</th>
                <th>Email</th>
                <th>Função</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {usuarios.map((u: any) => (
                <tr key={u.id}>
                  <td>{u.name}</td>
                  <td>{u.email}</td>
                  <td>{u.role}</td>
                  <td>
                    <button
                      className="btn btn-sm btn-danger"
                      onClick={() => excluirUsuario(u.id)}
                    >
                      Excluir
                    </button>
                  </td>
                </tr>
              ))}
              {usuarios.length === 0 && (
                <tr>
                  <td colSpan={4} className="text-center">Nenhum usuário encontrado</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
