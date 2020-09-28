--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: action; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.action (
    name character varying NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.action OWNER TO postgres;

--
-- Name: action_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.action_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.action_id_seq OWNER TO postgres;

--
-- Name: action_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.action_id_seq OWNED BY public.action.id;


--
-- Name: animal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.animal (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.animal OWNER TO postgres;

--
-- Name: animal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.animal_id_seq OWNER TO postgres;

--
-- Name: animal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.animal_id_seq OWNED BY public.animal.id;


--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying NOT NULL,
    id_parent integer NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- Name: connection; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.connection (
    id integer NOT NULL,
    pseudo character varying NOT NULL,
    password character varying NOT NULL,
    e_mail character varying NOT NULL
);


ALTER TABLE public.connection OWNER TO postgres;

--
-- Name: connection_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.connection_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.connection_id_seq OWNER TO postgres;

--
-- Name: connection_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.connection_id_seq OWNED BY public.connection.id;


--
-- Name: flora; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.flora (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.flora OWNER TO postgres;

--
-- Name: flora_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.flora_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.flora_id_seq OWNER TO postgres;

--
-- Name: flora_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.flora_id_seq OWNED BY public.flora.id;


--
-- Name: inventaire; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inventaire (
    id_player integer NOT NULL,
    id_object integer NOT NULL,
    amount integer NOT NULL
);


ALTER TABLE public.inventaire OWNER TO postgres;

--
-- Name: object; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.object (
    id integer NOT NULL,
    id_action integer NOT NULL,
    id_category integer NOT NULL,
    name character varying NOT NULL,
    amount_min integer NOT NULL,
    amount_max integer NOT NULL,
    stamina integer,
    food integer,
    hydratation integer
);


ALTER TABLE public.object OWNER TO postgres;

--
-- Name: object_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.object_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.object_id_seq OWNER TO postgres;

--
-- Name: object_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.object_id_seq OWNED BY public.object.id;


--
-- Name: player; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.player (
    id integer NOT NULL,
    id_connection integer NOT NULL,
    avatar character varying NOT NULL,
    position_x integer NOT NULL,
    position_y integer NOT NULL,
    stamina integer NOT NULL,
    food integer NOT NULL,
    hydratation integer NOT NULL
);


ALTER TABLE public.player OWNER TO postgres;

--
-- Name: player_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_id_seq OWNER TO postgres;

--
-- Name: player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.player_id_seq OWNED BY public.player.id;


--
-- Name: recipe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipe (
    id integer NOT NULL,
    id_object integer NOT NULL,
    id_action integer NOT NULL
);


ALTER TABLE public.recipe OWNER TO postgres;

--
-- Name: recipe_object; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipe_object (
    id_recipe integer NOT NULL,
    id_object integer NOT NULL,
    amount integer NOT NULL
);


ALTER TABLE public.recipe_object OWNER TO postgres;

--
-- Name: registration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.registration (
    id integer NOT NULL,
    address text,
    name text,
    password text
);


ALTER TABLE public.registration OWNER TO postgres;

--
-- Name: registration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.registration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.registration_id_seq OWNER TO postgres;

--
-- Name: registration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.registration_id_seq OWNED BY public.registration.id;


--
-- Name: action id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.action ALTER COLUMN id SET DEFAULT nextval('public.action_id_seq'::regclass);


--
-- Name: animal id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animal ALTER COLUMN id SET DEFAULT nextval('public.animal_id_seq'::regclass);


--
-- Name: category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- Name: connection id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.connection ALTER COLUMN id SET DEFAULT nextval('public.connection_id_seq'::regclass);


--
-- Name: flora id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flora ALTER COLUMN id SET DEFAULT nextval('public.flora_id_seq'::regclass);


--
-- Name: object id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.object ALTER COLUMN id SET DEFAULT nextval('public.object_id_seq'::regclass);


--
-- Name: player id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player ALTER COLUMN id SET DEFAULT nextval('public.player_id_seq'::regclass);


--
-- Name: registration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registration ALTER COLUMN id SET DEFAULT nextval('public.registration_id_seq'::regclass);


--
-- Data for Name: action; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.action (name, id) FROM stdin;
cutting	2
digging	3
enlighting	4
cooking	5
mining	6
sleeping	7
thinking	9
concococting	10
crafting	1
grinding	11
slicing	8
planting	12
\.


--
-- Data for Name: animal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.animal (id, name) FROM stdin;
\.


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, name, id_parent) FROM stdin;
5	Fruit	2
6	Légume	2
7	Ressource	2
8	Plante	2
9	Consommable	9
11	Boisson	9
12	Nourriture	9
1	Outils	1
2	Ingrédient	2
3	Graine	3
4	Céréale	2
10	Concocoction	9
\.


--
-- Data for Name: connection; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.connection (id, pseudo, password, e_mail) FROM stdin;
2	Douze	Gamelle	Doudou@gmail.com
3	kagari	group12	azaidzj\t
7	laura	group12	zeaafa
9	bidule	group12	aleoaien
10	truc	group12	ajeua
11	jean	group12	aueuahe
14	laura	647dca49fd1d3f5532e4c08761fc6b4ebe7b9c47	laura.busignies@hotmail.com
17	benjamin	group12	busignies.laura@hotmail.com
\.


--
-- Data for Name: flora; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.flora (id, name) FROM stdin;
\.


--
-- Data for Name: inventaire; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.inventaire (id_player, id_object, amount) FROM stdin;
1	1	1
1	2	1
1	3	1
1	4	1
2	1	1
\.


--
-- Data for Name: object; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.object (id, id_action, id_category, name, amount_min, amount_max, stamina, food, hydratation) FROM stdin;
5	4	1	Torche	1	1	-5	0	0
6	9	1	Canne à pêche	1	1	5	0	0
7	10	1	Concococteur	1	1	-5	0	0
19	1	5	Noix de coco	1	1	-10	30	10
23	1	5	Banane	2	6	20	50	0
26	1	6	Carotte	1	3	10	45	0
30	10	1	Récipient	1	2	-10	0	0
31	5	8	Ortie	2	6	0	15	3
32	5	8	Champignon Blanc	2	5	-15	-5	2
33	5	8	Champignon Marron	2	5	2	2	2
34	5	8	Champignon Rouge	3	6	-30	-15	-20
45	10	8	Fleur Blanche	2	4	10	10	10
46	10	8	Fleur Violette	2	4	0	0	0
52	12	3	Graine de cocotiers	1	1	0	3	3
56	12	3	Graine de bananes	1	1	0	4	4
57	12	3	Graine de carottes	1	1	0	1	2
9	7	1	Lit	1	1	100	-10	-10
35	5	8	Baie	6	10	10	30	5
1	2	1	Hachette	1	1	-5	0	0
2	3	1	Pelle	1	1	-5	0	0
3	6	1	Pioche	1	1	-5	0	0
4	8	1	Serpe	1	1	-5	0	0
10	1	7	Bois	3	8	0	0	0
11	1	7	Silex	3	8	0	0	0
12	1	7	Liane	2	6	0	0	0
13	1	7	Pierre	2	6	0	0	0
14	1	7	Sève	1	4	0	0	0
15	1	7	Laine	2	10	0	0	0
16	1	7	Feuille	2	8	0	0	0
17	1	7	Eau	1	10	10	0	50
18	1	7	Jus de coco	1	3	10	10	30
8	5	1	Campfire	1	1	0	0	0
20	10	9	Potion de force	1	1	75	0	0
21	10	9	Potion nutritive	1	1	0	75	0
22	10	9	Potion hydratante	1	1	0	0	75
24	10	9	Potion parfaite	1	1	50	50	50
50	12	3	Soupe	1	1	25	25	35
\.


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player (id, id_connection, avatar, position_x, position_y, stamina, food, hydratation) FROM stdin;
16	10	avatar1	9000	9000	100	100	100
3	7	avatar7	9908	8967	25	25	56
2	2	avatar5	9000	3000	100	100	100
15	9	avatar5	0	0	100	100	100
20	17	avatar6	3788	10988	100	100	100
1	3	avatar2	5916	2420	24	100	56
\.


--
-- Data for Name: recipe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipe (id, id_object, id_action) FROM stdin;
1	1	1
2	2	1
3	3	1
4	4	1
5	5	1
6	6	1
7	7	1
8	8	1
9	9	1
10	18	1
11	20	10
12	21	10
13	22	10
14	24	10
15	30	1
16	50	1
17	52	1
18	56	1
19	57	1
\.


--
-- Data for Name: recipe_object; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipe_object (id_recipe, id_object, amount) FROM stdin;
1	10	4
1	11	2
1	12	2
2	10	3
2	13	1
2	12	1
3	10	3
3	11	4
3	12	2
4	10	1
4	11	2
4	12	1
5	10	3
5	14	2
5	16	1
6	10	1
6	12	1
6	13	1
7	19	1
8	13	5
8	14	3
8	30	1
9	10	4
9	12	4
9	16	6
11	32	2
11	35	2
11	45	2
12	33	2
12	46	2
12	35	2
13	34	2
13	35	2
13	45	2
14	20	1
14	21	1
14	22	1
10	19	1
15	19	1
16	17	1
16	26	2
16	31	4
16	23	2
17	19	1
18	23	1
19	26	1
\.


--
-- Data for Name: registration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.registration (id, address, name, password) FROM stdin;
1	libor.alex@gmail.com	Alex	Libor
2	libor.alex@gmail.com	alors	Libor
3	euh@quoi.fr	Youpi	tralala
4	lom@gmail.com	aller	psg4ever
5	lom@gmail.com	aller	psg4ever
6	lom@gmail.com	aller	psg4ever
7	lom@gmail.com	aller	psg4ever
8	lom@gmail.com	aller	psg4ever
9	lom@gmail.com	aller	psg4ever
10	lom@gmail.com	aller	psg4ever
11	lom@gmail.com	aller	psg4ever
12	lom@gmail.com	aller	psg4ever
13	lom@gmail.com	aller	psg4ever
14	lom@gmail.com	aller	psg4ever
15	lom@gmail.com	aller	psg4ever
16	lom@gmail.com	aller	psg4ever
17	lom@gmail.com	aller	psg4ever
18	lom@gmail.com	aller	psg4ever
19	lom@gmail.com	aller	psg4ever
20	lom@gmail.com	aller	psg4ever
21	lom@gmail.com	aller	psg4ever
22	lom@gmail.com	aller	psg4ever
23	lom@gmail.com	aller	psg4ever
24	lom@gmail.com	aller	psg4ever
\.


--
-- Name: action_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.action_id_seq', 12, true);


--
-- Name: animal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.animal_id_seq', 1, false);


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- Name: connection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.connection_id_seq', 17, true);


--
-- Name: flora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flora_id_seq', 1, false);


--
-- Name: object_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.object_id_seq', 24, true);


--
-- Name: player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.player_id_seq', 20, true);


--
-- Name: registration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.registration_id_seq', 24, true);


--
-- Name: action action_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.action
    ADD CONSTRAINT action_pk PRIMARY KEY (id);


--
-- Name: animal animal_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_pk PRIMARY KEY (id);


--
-- Name: category category_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pk PRIMARY KEY (id);


--
-- Name: connection connection_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.connection
    ADD CONSTRAINT connection_pk PRIMARY KEY (id);


--
-- Name: flora flora_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flora
    ADD CONSTRAINT flora_pk PRIMARY KEY (id);


--
-- Name: object object_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.object
    ADD CONSTRAINT object_pk PRIMARY KEY (id);


--
-- Name: player player_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pk PRIMARY KEY (id);


--
-- Name: recipe recipe_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe
    ADD CONSTRAINT recipe_pk PRIMARY KEY (id);


--
-- Name: registration registration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.registration
    ADD CONSTRAINT registration_pkey PRIMARY KEY (id);


--
-- Name: category category_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_fk FOREIGN KEY (id_parent) REFERENCES public.category(id);


--
-- Name: inventaire inventaire_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventaire
    ADD CONSTRAINT inventaire_fk FOREIGN KEY (id_object) REFERENCES public.object(id);


--
-- Name: inventaire inventaire_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventaire
    ADD CONSTRAINT inventaire_fk_1 FOREIGN KEY (id_player) REFERENCES public.player(id);


--
-- Name: object object_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.object
    ADD CONSTRAINT object_fk FOREIGN KEY (id_action) REFERENCES public.action(id);


--
-- Name: object object_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.object
    ADD CONSTRAINT object_fk_1 FOREIGN KEY (id_category) REFERENCES public.category(id);


--
-- Name: player player_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_fk FOREIGN KEY (id_connection) REFERENCES public.connection(id);


--
-- Name: recipe recipe_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe
    ADD CONSTRAINT recipe_fk FOREIGN KEY (id_action) REFERENCES public.action(id);


--
-- Name: recipe recipe_fk0; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe
    ADD CONSTRAINT recipe_fk0 FOREIGN KEY (id_object) REFERENCES public.object(id);


--
-- Name: recipe_object recipe_object_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_object
    ADD CONSTRAINT recipe_object_fk FOREIGN KEY (id_object) REFERENCES public.object(id);


--
-- Name: recipe_object recipe_object_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe_object
    ADD CONSTRAINT recipe_object_fk_1 FOREIGN KEY (id_recipe) REFERENCES public.recipe(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA public TO pg_write_server_files;
GRANT ALL ON SCHEMA public TO pg_stat_scan_tables;
GRANT ALL ON SCHEMA public TO pg_signal_backend;
GRANT ALL ON SCHEMA public TO pg_read_server_files;
GRANT ALL ON SCHEMA public TO pg_read_all_stats;
GRANT ALL ON SCHEMA public TO pg_read_all_settings;
GRANT ALL ON SCHEMA public TO pg_monitor;
GRANT ALL ON SCHEMA public TO pg_execute_server_program;


--
-- PostgreSQL database dump complete
--

