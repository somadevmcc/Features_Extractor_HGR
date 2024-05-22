
Instrucciones de uso:
1.- Asegurar tener Docker desktop(o equivalente en linux) abierto
2.- Abrir la raíz del proyecto
3.- Abrir una terminal en la ruta raíz del proyecto
4.- Escribir "docker compose build"
5.- Esperar que se construya el contenedor
6.- Cuando termine escribir "docker compose up" para ejecutar

Caso especial:
Esta herramienta espera que tengas una GPU nvidia para funcionar
En caso de no contar con una entonces debes modificar

El archivo 'DensePose\dense.py'
    buscar la (20) linea self.cfg.MODEL.DEVICE = 0 y cambiarla por self.cfg.MODEL.DEVICE = 'cpu'
Tambien el archivo 'detectron2\detectron.py'
    buscar la (19) linea self.cfg.MODEL.DEVICE = 0 y cambiarla por self.cfg.MODEL.DEVICE = 'cpu'

Notas:
Los videos deben ir en la carpeta "video-inputs"
Debes modificar el main.py para cambiar la ruta del video a procesar
    video_path = "video-inputs/tu-video.avi" //Ruta del video
    name = "tu-video" //Nombre de los archivos a generar 

La herramienta genera un video en la ruta "video-output/tu-video/mask.avi"
e imprime los puntos claves en las siguientes rutas:
    csvs/angles/tu-video
    csvs/keypoints/tu-video
