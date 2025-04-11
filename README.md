# Sistema CME (Central de Materiais e Esterilização)

Este projeto é um sistema web desenvolvido como parte do Desafio Técnico Full Stack do Grupo Bringel. O objetivo é auxiliar no controle e rastreabilidade de materiais hospitalares esterilizados.

## 🧩 Tecnologias Utilizadas

- **Frontend**: React + Vite + TypeScript + Bootstrap
- **Backend**: Python + FastAPI + SQLAlchemy + JWT Auth
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker + Docker Compose

---

## 🧠 Funcionalidades

### 👤 Gerenciamento de Usuários

- **Administrador**:
  - Cadastra novos usuários (admin, técnico e enfermagem)
  - Gerencia usuários existentes

- **Técnico**:
  - Cadastra materiais
  - Registra etapas do processo de esterilização

- **Enfermagem**:
  - Consulta rastreabilidade dos materiais
  - Gera relatórios PDF/XLSX

### 📦 Cadastro de Materiais

- Nome
- Tipo
- Validade
- Serial gerado automaticamente

### 🔁 Processo de Esterilização

Os materiais passam pelas seguintes etapas:

1. Recebimento
2. Lavagem
3. Esterilização
4. Distribuição

Cada etapa pode ter status `concluído` ou `falha`.

### 🔎 Rastreabilidade

- Filtrar histórico de etapas por serial
- Visualizar falhas associadas a um serial
- Contagem de ciclos completos (4 etapas = 1 ciclo)
- Exportar relatórios em PDF ou XLSX

---

## 📁 Estrutura do Projeto

```
cme-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   └── process.py
│   │   ├── routes/
│   │   │   ├── user_routes.py
│   │   │   └── process_routes.py
│   │   ├── repositories/
│   │   │   ├── user_repository.py
│   │   │   └── process_repository.py
│   │   ├── utils/
│   │   │   ├── auth.py
│   │   │   ├── serial_generator.py
│   │   │   ├── xlsx_generator.py
│   │   │   └── pdf_generator.py
│   │   └── database.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Login.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Materiais/
│   │   │   │   └── MateriaisPage.tsx
│   │   │   ├── Processos/
│   │   │   │   ├── RegistroProcessoPage.tsx
│   │   │   │   └── MeusProcessosPage.tsx
│   │   │   ├── Rastreabilidade/
│   │   │   │   └── RastreabilidadePage.tsx
│   │   │   ├── Relatorios/
│   │   │   │   └── RelatoriosPage.tsx
│   │   │   └── Usuarios/
│   │   │       └── UsuariosPage.tsx
│   │   ├── routes/
│   │   │   ├── AppRoutes.tsx
│   │   │   └── PrivateRoute.tsx
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── vite-env.d.ts
│   ├── Dockerfile
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── docker-compose.yml
├── README.md
└── .gitignore

```

## Arquitetura do Sistema
![Arquitetura do Sistema](https://github.com/paulovitor21/cme-system/blob/main/docs/arquitetura_cme.png)


# Sistema CME - Central de Materiais e Esterilização

Este projeto é um sistema para controle e rastreabilidade de materiais hospitalares esterilizados, desenvolvido como desafio técnico do Grupo Bringel.

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

```
    git clone https://github.com/seu-usuario/cme-system.git
    cd cme-system
```
2. Execute os containers com Docker Compose:
```
    docker-compose up --build
```
3. Acesse:
    - Frontend: http://localhost:3000

    - Backend (Swagger): http://localhost:8000/docs

    - Banco de dados: PostgreSQL rodando em localhost:5432

### 📝 Considerações
| Funcionalidade                                             | Descrição                                                                 |
|------------------------------------------------------------|---------------------------------------------------------------------------|
| 🔐 Autenticação com JWT                                    | Controle de acesso baseado em token e papel do usuário (Role)            |
| 👤 Criação automática de admin                             | Primeiro usuário admin é criado automaticamente no backend               |
| 🔢 Geração de Serial Automático                            | Cada material recebe um serial gerado com base no nome                   |
| ✅ Commits Semânticos                                       | Histórico do projeto documentado com padrões de commit                   |
| 👥 Testado com Múltiplos Perfis                            | Usuários Técnico, Enfermagem e Administrativo testados

🧠 Desenvolvido por
- Paulo Vitor Pereira