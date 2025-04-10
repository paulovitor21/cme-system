// src/routes/AppRoutes.tsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import UsuariosPage from "../pages/Usuarios/UsuariosPage";
import MateriaisPage from "../pages/Materiais/MateriaisPage";
import RegistroProcessoPage from "../pages/Processos/RegistroProcessoPage";
import RastreabilidadePage from "../pages/Rastreabilidade/RastreabilidadePage";
import RelatoriosPage from "../pages/Relatorios/RelatoriosPage";
import { PrivateRoute } from "./PrivateRoute";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/usuarios"
          element={
            <PrivateRoute allowedRoles={["administrativo"]}>
              <UsuariosPage />
            </PrivateRoute>
          }
        />
        <Route
          path="/materiais"
          element={
            <PrivateRoute allowedRoles={["tecnico"]}>
              <MateriaisPage />
            </PrivateRoute>
          }
        />
        <Route 
        path="/processos" 
        element={
        <PrivateRoute>
          <RegistroProcessoPage />
          </PrivateRoute>
          } 
        />
        <Route
          path="/rastreabilidade"
          element={
            <PrivateRoute allowedRoles={["enfermagem"]}>
              <RastreabilidadePage />
            </PrivateRoute>
          }
        />
        <Route
          path="/relatorios"
          element={
            <PrivateRoute allowedRoles={["enfermagem"]}>
              <RelatoriosPage />
            </PrivateRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
