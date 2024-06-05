-- Table: ctl_angles

-- DROP TABLE IF EXISTS ctl_angles;

CREATE TABLE IF NOT EXISTS ctl_angles
(
    idu integer NOT NULL DEFAULT nextval('ctl_angles_idu_seq'::regclass),
    idu_etiqueta integer NOT NULL,
    frame integer NOT NULL,
    nose_mid_shoulder character varying(100) COLLATE pg_catalog."default" NOT NULL,
    mid_shoulder_mid_hip character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_shoulder_left_elbow character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_elbow_left_wrist character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_shoulder_right_elbow character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_elbow_right_wrist character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_hip_left_knee character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_knee_left_ankle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_hip_right_knee character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_knee_right_ankle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    mid_shoulder_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_shoulder_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_elbow_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_shoulder_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_elbow_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_hip_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    left_knee_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_hip_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    right_knee_angle character varying(100) COLLATE pg_catalog."default" NOT NULL,
    fecha_creacion date NOT NULL DEFAULT now(),
    fecha_modificacion date NOT NULL DEFAULT now(),
    activo boolean NOT NULL DEFAULT true,
    CONSTRAINT ctl_angles_pkey PRIMARY KEY (idu),
    CONSTRAINT idu_mascara FOREIGN KEY (idu_etiqueta)
        REFERENCES cat_etiquetas (idu) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);