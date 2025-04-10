```
    cme-system/
    │
    ├── backend/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── main.py                  # Arquivo principal da aplicação
    │   │   ├── database.py              # Configuração do banco de dados
    │   │   ├── models/
    │   │   │   ├── __init__.py
    │   │   │   ├── user.py              # Modelos de usuário
    │   │   │   └── material.py          # Modelos de materiais (a ser implementado)
    │   │   ├── repositories/
    │   │   │   ├── __init__.py
    │   │   │   ├── user_repository.py   # Repositório de usuários
    │   │   │   └── material_repository.py  # Repositório de materiais (a ser implementado)
    │   │   ├── routes/
    │   │   │   ├── __init__.py
    │   │   │   ├── user_routes.py       # Rotas de API para usuários
    │   │   │   └── material_routes.py   # Rotas de API para materiais (a ser implementado)
    │   │   └── utils/
    │   │       ├── __init__.py
    │   │       ├── auth.py              # Utilidades de autenticação
    │   │       └── pdf_generator.py     # Gerador de PDF (a ser implementado)
    │   ├── Dockerfile                   # Dockerfile do backend
    │   └── requirements.txt             # Dependências Python
    │
    ├── frontend/
    │   ├── public/
    │   │   ├── index.html
    │   │   └── favicon.ico
    │   ├── src/
    │   │   ├── components/
    │   │   │   ├── auth/
    │   │   │   │   ├── Login.jsx
    │   │   │   │   └── PrivateRoute.jsx
    │   │   │   ├── users/
    │   │   │   │   ├── UserForm.jsx
    │   │   │   │   ├── UserList.jsx
    │   │   │   │   └── UserDetails.jsx
    │   │   │   ├── materials/
    │   │   │   │   ├── MaterialForm.jsx
    │   │   │   │   ├── MaterialList.jsx
    │   │   │   │   └── MaterialDetails.jsx
    │   │   │   └── process/
    │   │   │       ├── ProcessSteps.jsx
    │   │   │       └── Tracking.jsx
    │   │   ├── services/
    │   │   │   ├── api.js
    │   │   │   ├── authService.js
    │   │   │   ├── userService.js
    │   │   │   └── materialService.js
    │   │   ├── context/
    │   │   │   └── AuthContext.js
    │   │   ├── App.jsx
    │   │   └── index.js
    │   ├── package.json
    │   └── Dockerfile                   # Dockerfile do frontend
    │
    ├── docker-compose.yml               # Configuração do Docker Compose
    └── README.md                        # Documentação do projeto
```

# Sistema CME - Central de Materiais e Esterilização

Este projeto é um sistema completo para controle e rastreabilidade de materiais hospitalares esterilizados, desenvolvido como desafio técnico do Grupo Bringel.

## 🔧 Tecnologias utilizadas

- **Backend:** Python + FastAPI
- **Frontend:** React + TypeScript + Vite
- **Banco de dados:** PostgreSQL
- **Autenticação:** JWT
- **Relatórios:** PDF (ReportLab) e XLSX (OpenPyXL)
- **Containers:** Docker + Docker Compose

---

## 📦 Funcionalidades

### 🔐 Login com autenticação JWT

### 🧑‍🔧 Técnico
- Cadastrar materiais
- Registrar etapas do processo (lavagem, esterilização etc.)

### 🧑‍⚕️ Enfermagem
- Consultar rastreabilidade por serial
- Gerar relatórios (PDF e Excel)

### 🧑‍💼 Administrativo
- Gerenciar usuários do sistema

---

## 🚀 Como executar o projeto

### Pré-requisitos
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/cme-system.git
cd cme-system
