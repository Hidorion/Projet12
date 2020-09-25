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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: action; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.action (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.action OWNER TO postgres;

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
    position_x integer,
    position_y integer NOT NULL
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
    name character varying NOT NULL,
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
-- Data for Name: action; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.action (id, name) FROM stdin;
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
\.


--
-- Data for Name: connection; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.connection (id, email, pseudo, password) FROM stdin;
2	onsenfout@gmail.com	Kosovo	Hachette
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
\.


--
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.player (id, id_connection, avatar, position_x, position_y) FROM stdin;
\.


--
-- Data for Name: recipe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipe (id, name, id_action) FROM stdin;
\.


--
-- Data for Name: recipe_object; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipe_object (id_recipe, id_object, amount) FROM stdin;
\.


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

SELECT pg_catalog.setval('public.connection_id_seq', 1, false);


--
-- Name: flora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flora_id_seq', 1, false);


--
-- Name: object_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.object_id_seq', 1, false);


--
-- Name: player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.player_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

