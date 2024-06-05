--DROP function fun_generar_reporte_angles()

CREATE OR REPLACE FUNCTION fun_generar_reporte_angles(
_etiqueta character varying,	
OUT etiqueta character varying,
OUT frame character varying,
OUT nose_mid_shoulder character varying,
OUT mid_shoulder_mid_hip character varying,
OUT left_shoulder_left_elbow character varying,
OUT left_elbow_left_wrist character varying,
OUT right_shoulder_right_elbow character varying,
OUT right_elbow_right_wrist character varying,
OUT left_hip_left_knee character varying,
OUT left_knee_left_ankle character varying,
OUT right_hip_right_knee character varying,
OUT right_knee_right_ankle character varying,
OUT mid_shoulder_angle character varying,
OUT left_shoulder_angle character varying,
OUT left_elbow_angle character varying,
OUT right_shoulder_angle character varying,
OUT right_elbow_angle character varying,
OUT left_hip_angle character varying,
OUT left_knee_angle character varying,
OUT right_hip_angle character varying,
OUT right_knee_angle character varying
)
RETURNS SETOF record
LANGUAGE 'plpgsql'

AS $BODY$

DECLARE
reg RECORD;
	BEGIN 

		for reg in (
			select a.nombre as etiqueta,
			b.frame,
			b.nose_mid_shoulder,
			b.mid_shoulder_mid_hip,
			b.left_shoulder_left_elbow,
			b.left_elbow_left_wrist,
			b.right_shoulder_right_elbow,
			b.right_elbow_right_wrist,
			b.left_hip_left_knee,
			b.left_knee_left_ankle,
			b.right_hip_right_knee,
			b.right_knee_right_ankle,
			b.mid_shoulder_angle,
			b.left_shoulder_angle,
			b.left_elbow_angle,
			b.right_shoulder_angle,
			b.right_elbow_angle,
			b.left_hip_angle,
			b.left_knee_angle,
			b.right_hip_angle,
			b.right_knee_angle
			from
			cat_etiquetas a
			inner join
			ctl_angles b
			ON
			a.idu = b.idu_etiqueta
			WHERE a.nombre ilike _etiqueta AND b.activo = true 
			ORDER BY
			idu_etiqueta, frame
		)
		LOOP
			 etiqueta 					:= reg.etiqueta;
			 frame                      := reg.frame;
			 nose_mid_shoulder          := reg.nose_mid_shoulder;
			 mid_shoulder_mid_hip       := reg.mid_shoulder_mid_hip;
			 left_shoulder_left_elbow   := reg.left_shoulder_left_elbow;
			 left_elbow_left_wrist      := reg.left_elbow_left_wrist;
			 right_shoulder_right_elbow := reg.right_shoulder_right_elbow;
			 right_elbow_right_wrist    := reg.right_elbow_right_wrist;
			 left_hip_left_knee         := reg.left_hip_left_knee;
			 left_knee_left_ankle       := reg.left_knee_left_ankle;
			 right_hip_right_knee       := reg.right_hip_right_knee;
			 right_knee_right_ankle     := reg.right_knee_right_ankle;
			 mid_shoulder_angle         := reg.mid_shoulder_angle;
			 left_shoulder_angle        := reg.left_shoulder_angle;
			 left_elbow_angle           := reg.left_elbow_angle;
			 right_shoulder_angle       := reg.right_shoulder_angle;
			 right_elbow_angle          := reg.right_elbow_angle;
			 left_hip_angle             := reg.left_hip_angle;
			 left_knee_angle            := reg.left_knee_angle;
			 right_hip_angle            := reg.right_hip_angle;
			 right_knee_angle           := reg.right_knee_angle;
			RETURN NEXT;
		END LOOP;

	END;

$BODY$;
			


