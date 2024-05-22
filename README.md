Instrucciones de uso:
1.- Asegurar tener Docker desktop(o equivalente en linux) abierto
2.- Abrir la raíz del proyecto
3.- Abrir una terminal en la ruta raíz del proyecto
4.- Escribir "docker compose build"
5.- Esperar que se construya el contenedor
6.- Cuando termine escribir "docker compose up" para ejecutar


Notas:
Los videos deben ir en la carpeta "video-inputs"
Debes modificar el main.py para cambiar la ruta del video a procesar
    video_path = "video-inputs/tu-video.avi" //Ruta del video
    name = "tu-video" //Nombre de los archivos a generar 

La herramienta genera un video en la ruta "video-output/tu-video/mask.avi"
e imprime los puntos claves en las siguientes rutas:
    csvs/angles/tu-video
    csvs/keypoints/tu-video
