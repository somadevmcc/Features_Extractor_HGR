--DROP function fun_generar_reporte_keypoints()

CREATE OR REPLACE FUNCTION fun_generar_reporte_keypoints(
OUT etiqueta character varying,
OUT frame character varying,
OUT nose character varying,
OUT left_shoulder character varying,
OUT right_shoulder character varying,
OUT left_elbow character varying,
OUT right_elbow character varying,
OUT left_wrist character varying,
OUT right_wrist character varying,
OUT left_hip character varying,
OUT right_hip character varying,
OUT left_knee character varying,
OUT right_knee character varying,
OUT left_ankle character varying,
OUT right_ankle character varying,
OUT mid_shoulder character varying,
OUT mid_hip character varying
)
RETURNS SETOF record
LANGUAGE 'plpgsql'

AS $BODY$

DECLARE
reg RECORD;
	BEGIN 

		for reg in (
			select a.nombre as etiqueta,  b.frame , b.nose , b.left_shoulder , b.right_shoulder , b.left_elbow , b.right_elbow , b.left_wrist , b.right_wrist , b.left_hip , b.right_hip , b.left_knee , b.right_knee , b.left_ankle , b.right_ankle , b.mid_shoulder , b.mid_hip 
			from
			cat_etiquetas a
			inner join
			ctl_keypoints b
			ON
			a.idu = b.idu_etiqueta
			WHERE b.activo = true
			ORDER BY
			idu_etiqueta, frame
		)
		LOOP
			etiqueta := reg.etiqueta;
			frame := reg.frame;
			nose := reg.nose;
			left_shoulder := reg.left_shoulder;
			right_shoulder := reg.right_shoulder;
			left_elbow := reg.left_elbow;
			right_elbow := reg.right_elbow;
			left_wrist := reg.left_wrist;
			right_wrist := reg.right_wrist;
			left_hip := reg.left_hip;
			right_hip := reg.right_hip;
			left_knee := reg.left_knee;
			right_knee := reg.right_knee;
			left_ankle := reg.left_ankle;
			right_ankle := reg.right_ankle;
			mid_shoulder := reg.mid_shoulder;
			mid_hip		:= reg.mid_hip;
			RETURN NEXT;
		END LOOP;

	END;

$BODY$;
			


