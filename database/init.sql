--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4 (Debian 17.4-1.pgdg120+2)
-- Dumped by pg_dump version 17.4 (Debian 17.4-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: etapaenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.etapaenum AS ENUM (
    'RECEBIMENTO',
    'LAVAGEM',
    'ESTERILIZACAO',
    'DISTRIBUICAO'
);


ALTER TYPE public.etapaenum OWNER TO postgres;

--
-- Name: statusenum; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.statusenum AS ENUM (
    'CONCLUIDO',
    'FALHA'
);


ALTER TYPE public.statusenum OWNER TO postgres;

--
-- Name: userrole; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.userrole AS ENUM (
    'ADMIN',
    'NURSE',
    'TECHNICIAN'
);


ALTER TYPE public.userrole OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: materiais; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.materiais (
    id character varying NOT NULL,
    nome character varying NOT NULL,
    tipo character varying NOT NULL,
    data_validade date NOT NULL,
    serial character varying NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.materiais OWNER TO postgres;

--
-- Name: processos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.processos (
    id character varying NOT NULL,
    serial character varying NOT NULL,
    etapa public.etapaenum NOT NULL,
    status public.statusenum NOT NULL,
    descricao_falha character varying,
    usuario_id character varying NOT NULL,
    data_hora timestamp without time zone
);


ALTER TABLE public.processos OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying NOT NULL,
    name character varying NOT NULL,
    email character varying NOT NULL,
    password_hash character varying NOT NULL,
    role public.userrole NOT NULL,
    is_active boolean,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: materiais; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.materiais (id, nome, tipo, data_validade, serial, created_at) FROM stdin;
83fd0be3-38a8-4642-9475-7ec0d53f5dbc	pinca_cirurgica	instrumento	2025-04-08	PINCA_CIRURGICA-101994	2025-04-08 22:25:59.293328
f97cec55-a96f-4c70-a705-91d21918a59f	Pinca Hemostatica	Instrumento	2025-12-31	PINCA-HEMOSTATICA-393508	2025-04-08 22:31:47.93119
d26740ae-7802-412e-ba62-1e08eed3708a	Bisturi	Intrumento	2025-04-09	BISTURI-859520	2025-04-09 14:15:50.775609
af183fe1-aaff-4099-a0c7-ebdb2779dd9d	Porta-agulhas	Instrumento	2025-04-09	PORTA-AGULHAS-591177	2025-04-09 23:19:32.243222
a2abe9ad-d1ce-4ef6-a855-80acaefc42e0	Tesoura	Instrumento	2025-04-10	TESOURA-998674	2025-04-10 18:12:20.811754
f6edd2bf-efa1-43b8-b27a-fc3a1923191e	Flebo	Instrumento	2025-04-11	FLEBO-834269	2025-04-11 12:23:46.282823
\.


--
-- Data for Name: processos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.processos (id, serial, etapa, status, descricao_falha, usuario_id, data_hora) FROM stdin;
bc3c8e95-04c7-4845-ad47-d706067a7ba2	PINCA-CIRURGICA-123456	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 13:04:28.466657
7458885a-e9a6-42ce-9385-f9f5f0984463	PINCA-CIRURGICA-123456	LAVAGEM	FALHA	Equipamento com sujeira	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 13:11:59.310851
f1f78993-8842-4e4c-8208-4f0a61393cbf	PINCA-CIRURGICA-123456	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 13:38:16.503147
32735272-c565-4a79-bdff-f38c4d3e8682	PINCA-CIRURGICA-123456	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 13:41:25.626767
60961f0f-89b7-4ea4-a011-cedee06e5065	PINCA-CIRURGICA-1234567	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 13:42:20.764543
c8b88409-70c7-4bc3-9bf6-b4822b6db458	PINCA_CIRURGICA-101994	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 13:50:05.446335
ed113a4e-84d8-4a38-b0d0-4be6517adbe0	BISTURI-859520	RECEBIMENTO	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-09 14:18:20.020913
7d49d161-6071-428c-a525-7e01cab5d6f7	PORTA-AGULHAS-591177	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-10 11:17:48.83079
4c4dd5ed-9df6-4950-ace3-6edb152ab4a4	TESOURA-998674	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-10 18:41:03.5752
9ae4c47c-bf57-48b0-95b6-112cb59915a3	TESOURA-998674	ESTERILIZACAO	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-10 18:41:20.924572
8e4907ea-9b44-4ae2-abd3-30b5254aa909	FLEBO-834269	RECEBIMENTO	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-11 12:25:38.219513
e3d7fe21-57fe-4369-b951-a1a2c5366a10	FLEBO-834269	LAVAGEM	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-11 12:25:56.646376
422c20e5-7bb6-480a-b5b3-e8f4b3d16bb6	FLEBO-834269	ESTERILIZACAO	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-11 12:26:03.036772
0e3f4e53-984e-4c92-bca0-d3b106ccc9e7	FLEBO-834269	DISTRIBUICAO	CONCLUIDO	\N	42a9dd18-83b1-44a3-be0d-80a7a2a890ca	2025-04-11 12:26:09.706842
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, email, password_hash, role, is_active, created_at, updated_at) FROM stdin;
21f9e351-b173-41af-9f60-ef233078cfbf	Admin	admin@cme.com	$2b$12$FNO8bHTwrbNg3wCs6xFTKu2bPTJhCFMzp5Feg/sOqNlgjr11ymoH2	ADMIN	t	2025-04-08 22:22:03.310468	2025-04-08 22:22:03.310471
42a9dd18-83b1-44a3-be0d-80a7a2a890ca	bruna	bruna@cme.com	$2b$12$RKO/dV2/dcvVmCZd8jF4SOD0HwNxoP5jVRlYlnNiCC9CH.qN7IPHq	TECHNICIAN	t	2025-04-08 22:23:52.975616	2025-04-08 22:23:52.975619
e854ca7c-3df3-4bee-99c2-b511e8585d5d	paulo	paulo@cme.com	$2b$12$z2bYP75DlPUGkWAayoedqO3UV9bUPAR9oXloTcGhUi1A9L9FiIcZe	TECHNICIAN	t	2025-04-10 14:55:28.393182	2025-04-10 14:55:28.393188
5318b7b0-d38f-4e91-86c4-456cb4dfc52b	mari	mari@cme.com	$2b$12$QloxyT1CslrIv09azw/AveO5kYvnI3DnDpjezW8wFGIxiFQa2Ovqe	NURSE	t	2025-04-10 14:57:50.799368	2025-04-10 14:57:50.79937
b6aaa104-4836-43cc-88b4-03fc9b628897	Jose	jose@cme.com	$2b$12$Xvl.68PkHgT9hwhJJYBWaO.l37ghE9r0.StEmef2elVVZouMaPdyW	NURSE	t	2025-04-10 20:11:49.612845	2025-04-10 20:11:49.612848
\.


--
-- Name: materiais materiais_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materiais
    ADD CONSTRAINT materiais_pkey PRIMARY KEY (id);


--
-- Name: processos processos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.processos
    ADD CONSTRAINT processos_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_materiais_serial; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_materiais_serial ON public.materiais USING btree (serial);


--
-- Name: ix_processos_serial; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_processos_serial ON public.processos USING btree (serial);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: processos processos_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.processos
    ADD CONSTRAINT processos_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

