-- Table: cat_etiquetas

-- DROP TABLE IF EXISTS cat_etiquetas;

CREATE TABLE IF NOT EXISTS cat_etiquetas
(
    idu integer NOT NULL DEFAULT nextval('cat_etiquetas_idu_seq'::regclass),
    nombre character varying(50) COLLATE pg_catalog."default" NOT NULL,
    fecha_creacion date NOT NULL DEFAULT now(),
    fecha_modificacion date NOT NULL DEFAULT now(),
    activo boolean NOT NULL DEFAULT true,
    CONSTRAINT cat_mascaras_pkey PRIMARY KEY (idu)
);