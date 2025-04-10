// src/pages/Teste.tsx
import React, { useEffect } from 'react';

export default function Teste() {
  useEffect(() => {
    console.log("API URL:", import.meta.env.VITE_API_URL);
  }, []);

  return <div>Testando variável de ambiente</div>;
}
