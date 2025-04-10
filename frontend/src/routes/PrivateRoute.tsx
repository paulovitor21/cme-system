// src/routes/PrivateRoute.tsx
import { JSX } from "react";
import { Navigate } from "react-router-dom";

interface PrivateRouteProps {
  children: JSX.Element;
  allowedRoles?: string[]; // ← novo
}

export function PrivateRoute({ children, allowedRoles }: PrivateRouteProps) {
  const token = localStorage.getItem("token");
  const role = localStorage.getItem("role");

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  if (allowedRoles && !allowedRoles.includes(role || "")) {
    return <Navigate to="/dashboard" replace />;
  }

  return children;
}
