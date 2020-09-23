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
-- Name: dojo_animal; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA dojo_animal;


ALTER SCHEMA dojo_animal OWNER TO postgres;

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
-- Name: animal; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.animal (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    id_type integer NOT NULL
);


ALTER TABLE dojo_animal.animal OWNER TO postgres;

--
-- Name: animal_id_seq; Type: SEQUENCE; Schema: dojo_animal; Owner: postgres
--

CREATE SEQUENCE dojo_animal.animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE dojo_animal.animal_id_seq OWNER TO postgres;

--
-- Name: animal_id_seq; Type: SEQUENCE OWNED BY; Schema: dojo_animal; Owner: postgres
--

ALTER SEQUENCE dojo_animal.animal_id_seq OWNED BY dojo_animal.animal.id;


--
-- Name: animal_zone; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.animal_zone (
    id_animal integer NOT NULL,
    id_zone integer NOT NULL
);


ALTER TABLE dojo_animal.animal_zone OWNER TO postgres;

--
-- Name: animal_zone_contact; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.animal_zone_contact (
    id_animal integer NOT NULL,
    id_contact integer NOT NULL,
    id_zone integer NOT NULL,
    date_obs date NOT NULL,
    quantity_male integer DEFAULT 0 NOT NULL,
    quantity_female integer DEFAULT 0 NOT NULL
);


ALTER TABLE dojo_animal.animal_zone_contact OWNER TO postgres;

--
-- Name: contact; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.contact (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);


ALTER TABLE dojo_animal.contact OWNER TO postgres;

--
-- Name: contact_id_seq; Type: SEQUENCE; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE dojo_animal.contact ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME dojo_animal.contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: country; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.country (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);


ALTER TABLE dojo_animal.country OWNER TO postgres;

--
-- Name: country_id_seq; Type: SEQUENCE; Schema: dojo_animal; Owner: postgres
--

CREATE SEQUENCE dojo_animal.country_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE dojo_animal.country_id_seq OWNER TO postgres;

--
-- Name: country_id_seq; Type: SEQUENCE OWNED BY; Schema: dojo_animal; Owner: postgres
--

ALTER SEQUENCE dojo_animal.country_id_seq OWNED BY dojo_animal.country.id;


--
-- Name: type; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.type (
    id integer NOT NULL,
    name character varying(30) NOT NULL,
    id_parent integer
);


ALTER TABLE dojo_animal.type OWNER TO postgres;

--
-- Name: type_id_seq; Type: SEQUENCE; Schema: dojo_animal; Owner: postgres
--

CREATE SEQUENCE dojo_animal.type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE dojo_animal.type_id_seq OWNER TO postgres;

--
-- Name: type_id_seq; Type: SEQUENCE OWNED BY; Schema: dojo_animal; Owner: postgres
--

ALTER SEQUENCE dojo_animal.type_id_seq OWNED BY dojo_animal.type.id;


--
-- Name: zone; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.zone (
    id integer NOT NULL,
    name character varying(30) NOT NULL
);


ALTER TABLE dojo_animal.zone OWNER TO postgres;

--
-- Name: zone_country; Type: TABLE; Schema: dojo_animal; Owner: postgres
--

CREATE TABLE dojo_animal.zone_country (
    id_zone integer NOT NULL,
    id_country integer NOT NULL
);


ALTER TABLE dojo_animal.zone_country OWNER TO postgres;

--
-- Name: zone_id_seq; Type: SEQUENCE; Schema: dojo_animal; Owner: postgres
--

CREATE SEQUENCE dojo_animal.zone_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE dojo_animal.zone_id_seq OWNER TO postgres;

--
-- Name: zone_id_seq; Type: SEQUENCE OWNED BY; Schema: dojo_animal; Owner: postgres
--

ALTER SEQUENCE dojo_animal.zone_id_seq OWNED BY dojo_animal.zone.id;


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
    email integer NOT NULL,
    pseudo character varying NOT NULL,
    password character varying NOT NULL
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
    amount_max integer NOT NULL
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
-- Name: animal id; Type: DEFAULT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal ALTER COLUMN id SET DEFAULT nextval('dojo_animal.animal_id_seq'::regclass);


--
-- Name: country id; Type: DEFAULT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.country ALTER COLUMN id SET DEFAULT nextval('dojo_animal.country_id_seq'::regclass);


--
-- Name: type id; Type: DEFAULT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.type ALTER COLUMN id SET DEFAULT nextval('dojo_animal.type_id_seq'::regclass);


--
-- Name: zone id; Type: DEFAULT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.zone ALTER COLUMN id SET DEFAULT nextval('dojo_animal.zone_id_seq'::regclass);


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
-- Data for Name: animal; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.animal (id, name, id_type) FROM stdin;
\.


--
-- Data for Name: animal_zone; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.animal_zone (id_animal, id_zone) FROM stdin;
\.


--
-- Data for Name: animal_zone_contact; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.animal_zone_contact (id_animal, id_contact, id_zone, date_obs, quantity_male, quantity_female) FROM stdin;
\.


--
-- Data for Name: contact; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.contact (id, name) FROM stdin;
\.


--
-- Data for Name: country; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.country (id, name) FROM stdin;
\.


--
-- Data for Name: type; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.type (id, name, id_parent) FROM stdin;
\.


--
-- Data for Name: zone; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.zone (id, name) FROM stdin;
\.


--
-- Data for Name: zone_country; Type: TABLE DATA; Schema: dojo_animal; Owner: postgres
--

COPY dojo_animal.zone_country (id_zone, id_country) FROM stdin;
\.


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

COPY public.connection (id, email, pseudo, password) FROM stdin;
1	onsenfout@gmail.com	'Kosovo'	'Hachette'
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
\.


--
-- Data for Name: object; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.object (id, id_action, id_category, name, amount_min, amount_max) FROM stdin;
1	2	1	Hachette	1	1
2	3	1	Pelle	1	1
3	6	1	Pioche	1	1
4	8	1	Serpe	1	1
5	4	1	Torche	1	1
6	9	1	Canne à pêche	1	1
7	10	1	Concococteur	1	1
8	5	1	Feu de camp	1	1
9	7	1	Lit de fortune	1	1
10	1	7	Bois	3	8
11	1	7	Silex	3	8
12	1	7	Liane	2	6
13	1	7	Pierre	2	6
14	1	7	Sève	1	4
15	1	7	Laine	2	10
16	1	7	Feuille	2	8
17	1	7	Eau	1	10
18	1	7	Jus de coco	1	3
19	1	5	Noix de coco	1	1
20	1	5	Melon	1	1
21	1	5	Ananas	1	1
22	1	5	Figue	1	3
23	1	5	Banane	2	6
24	1	4	Blé	10	20
25	1	4	Maïs	1	4
26	1	6	Carotte	1	3
27	1	6	Pomme de terre	2	6
28	1	6	Poireaux	1	1
29	1	6	Avocat	1	2
30	10	1	Récipient	1	2
31	5	8	Ortie	2	6
32	5	8	Champignon Blanc	2	5
33	5	8	Champignon Marron	2	5
34	5	8	Champignon Rouge	3	6
35	5	8	Baie Rouge	6	10
36	5	8	Baie Jaune	6	10
37	5	8	Baie Noire	6	10
38	5	8	Baie Bleue	6	10
39	10	8	Fleur Bleue	2	4
40	10	8	Fleur Rouge	2	4
41	10	8	Fleur Jaune	2	4
42	10	8	Fleur Rose	2	4
43	10	8	Fleur Verte	2	4
44	10	8	Fleur Noire	2	4
45	10	8	Fleur Blanche	2	4
46	10	8	Fleur Violette	2	4
47	12	3	Graine de fleurs	1	1
48	12	3	Graine de baies	1	1
49	12	3	Graine d'orties	1	1
50	12	3	Spore de champignons	1	1
51	12	3	Grain de céréales	1	1
52	12	3	Graine de cocotiers	1	1
53	12	3	Pépin de melons	1	1
54	12	3	Graine d'ananas	1	1
55	12	3	Pépin de figues	1	1
56	12	3	Graine de bananes	1	1
57	12	3	Graine de carottes	1	1
58	12	3	Graine de patates	1	1
59	12	3	Graine de poireaux	1	1
60	12	3	Noyau d'avocats	1	1
\.


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player (id, id_connection, avatar, position_x, position_y, stamina, food, hydratation) FROM stdin;
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
\.


--
-- Data for Name: recipe_object; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipe_object (id_recipe, id_object, amount) FROM stdin;
1	10	4
1	11	2
1	12	2
\.


--
-- Name: animal_id_seq; Type: SEQUENCE SET; Schema: dojo_animal; Owner: postgres
--

SELECT pg_catalog.setval('dojo_animal.animal_id_seq', 1, false);


--
-- Name: contact_id_seq; Type: SEQUENCE SET; Schema: dojo_animal; Owner: postgres
--

SELECT pg_catalog.setval('dojo_animal.contact_id_seq', 6, true);


--
-- Name: country_id_seq; Type: SEQUENCE SET; Schema: dojo_animal; Owner: postgres
--

SELECT pg_catalog.setval('dojo_animal.country_id_seq', 3, true);


--
-- Name: type_id_seq; Type: SEQUENCE SET; Schema: dojo_animal; Owner: postgres
--

SELECT pg_catalog.setval('dojo_animal.type_id_seq', 6, true);


--
-- Name: zone_id_seq; Type: SEQUENCE SET; Schema: dojo_animal; Owner: postgres
--

SELECT pg_catalog.setval('dojo_animal.zone_id_seq', 2, true);


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

SELECT pg_catalog.setval('public.category_id_seq', 12, true);


--
-- Name: connection_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.connection_id_seq', 1, false);


--
-- Name: flora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flora_id_seq', 1, false);


--
-- Name: object_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.object_id_seq', 60, true);


--
-- Name: player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.player_id_seq', 1, false);


--
-- Name: animal animal_pk; Type: CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal
    ADD CONSTRAINT animal_pk PRIMARY KEY (id);


--
-- Name: contact contact_pk; Type: CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.contact
    ADD CONSTRAINT contact_pk PRIMARY KEY (id);


--
-- Name: country country_pk; Type: CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.country
    ADD CONSTRAINT country_pk PRIMARY KEY (id);


--
-- Name: type type_pk; Type: CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.type
    ADD CONSTRAINT type_pk PRIMARY KEY (id);


--
-- Name: zone zone_pk; Type: CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.zone
    ADD CONSTRAINT zone_pk PRIMARY KEY (id);


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
-- Name: animal animal_FK; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal
    ADD CONSTRAINT "animal_FK" FOREIGN KEY (id_type) REFERENCES dojo_animal.type(id);


--
-- Name: animal_zone animal_zone_FK; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal_zone
    ADD CONSTRAINT "animal_zone_FK" FOREIGN KEY (id_zone) REFERENCES dojo_animal.zone(id);


--
-- Name: animal_zone animal_zone_FK_1; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal_zone
    ADD CONSTRAINT "animal_zone_FK_1" FOREIGN KEY (id_animal) REFERENCES dojo_animal.animal(id);


--
-- Name: animal_zone_contact animal_zone_contact_FK; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal_zone_contact
    ADD CONSTRAINT "animal_zone_contact_FK" FOREIGN KEY (id_animal) REFERENCES dojo_animal.animal(id);


--
-- Name: animal_zone_contact animal_zone_contact_FK_1; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal_zone_contact
    ADD CONSTRAINT "animal_zone_contact_FK_1" FOREIGN KEY (id_zone) REFERENCES dojo_animal.zone(id);


--
-- Name: animal_zone_contact animal_zone_contact_FK_2; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.animal_zone_contact
    ADD CONSTRAINT "animal_zone_contact_FK_2" FOREIGN KEY (id_contact) REFERENCES dojo_animal.contact(id);


--
-- Name: type type_FK; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.type
    ADD CONSTRAINT "type_FK" FOREIGN KEY (id_parent) REFERENCES dojo_animal.type(id);


--
-- Name: zone_country zone_country_FK; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.zone_country
    ADD CONSTRAINT "zone_country_FK" FOREIGN KEY (id_zone) REFERENCES dojo_animal.zone(id);


--
-- Name: zone_country zone_country_FK_1; Type: FK CONSTRAINT; Schema: dojo_animal; Owner: postgres
--

ALTER TABLE ONLY dojo_animal.zone_country
    ADD CONSTRAINT "zone_country_FK_1" FOREIGN KEY (id_country) REFERENCES dojo_animal.country(id);


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

