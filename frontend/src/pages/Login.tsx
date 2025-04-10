// src/pages/Login.tsx
import { useState } from "react";
import axios from "axios";

// const apiUrl = import.meta.env.VITE_API_URL;
const apiUrl = "http://localhost:8000/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [erro, setErro] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErro("");

    try {
      const formData = new URLSearchParams();
      formData.append("username", email);
      formData.append("password", senha);

      const response = await axios.post(`${apiUrl}/users/login`, formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      const { access_token, role, name, email: userEmail } = response.data;
      localStorage.setItem("token", access_token);
      localStorage.setItem("role", role);
      localStorage.setItem("name", name);
      localStorage.setItem("email", userEmail);
      
      // alert("Login realizado com sucesso!");
      window.location.href = "/dashboard";
    } catch (error: any) {
      setErro("Email ou senha inválidos");
    }
  };

  return (
    <div className="container d-flex justify-content-center align-items-center" style={{ height: "100vh" }}>
      <div className="card shadow p-4" style={{ width: 400 }}>
        <h2 className="text-center mb-4">Login - CME</h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">Email:</label>
            <input
              type="email"
              className="form-control"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Senha:</label>
            <input
              type="password"
              className="form-control"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              required
            />
          </div>
          {erro && <div className="alert alert-danger py-1">{erro}</div>}
          <button type="submit" className="btn btn-primary w-100">Entrar</button>
        </form>
      </div>
    </div>
  );
}
