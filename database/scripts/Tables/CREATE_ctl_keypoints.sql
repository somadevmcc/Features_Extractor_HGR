-- Table: ctl_keypoints

-- DROP TABLE IF EXISTS ctl_keypoints;

CREATE TABLE IF NOT EXISTS ctl_keypoints
(
    idu integer NOT NULL DEFAULT nextval('ctl_keypoints_idu_seq'::regclass),
    idu_etiqueta integer NOT NULL,
    frame integer NOT NULL,
    nose character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_shoulder character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_shoulder character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_elbow character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_elbow character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_wrist character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_wrist character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_hip character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_hip character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_knee character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_knee character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_ankle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_ankle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    mid_shoulder character varying(100) COLLATE pg_catalog."default" NOT NULL,
    mid_hip character varying(100) COLLATE pg_catalog."default" NOT NULL,
    fecha_creacion date NOT NULL DEFAULT now(),
    fecha_modificacion date NOT NULL DEFAULT now(),
    activo boolean NOT NULL DEFAULT true,
    CONSTRAINT ctl_mascaras_pkey PRIMARY KEY (idu),
    CONSTRAINT idu_mascara FOREIGN KEY (idu_etiqueta)
        REFERENCES cat_etiquetas (idu) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);