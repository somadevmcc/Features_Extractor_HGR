
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
import os
# Leer el archivo CSV
csv_file_path = r'C:\Users\luisf\Documents\GitHub\Features_Extractor_HGR\csvs\keypoints\fernando1\final_keypoints.csv'
data = pd.read_csv(csv_file_path)


# Ruta del directorio donde se guardarán las imágenes
output_dir = r'C:\Users\luisf\Documents\GitHub\Features_Extractor_HGR\csvs\keypoints\fernando1\seriesTiempo'

# Crear el directorio si no existe
os.makedirs(output_dir, exist_ok=True)

# Leer el archivo CSV
data = pd.read_csv(csv_file_path)

# Convertir las cadenas de texto de las columnas en numpy arrays
columns = ['nose', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 
           'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 
           'right_ankle', 'mid_shoulder', 'mid_hip']

for column in columns:
    data[column] = data[column].apply(lambda x: np.array(ast.literal_eval(x)))

# Dibujar el "mono de palitos" para cada frame y guardar la imagen
def plot_skeleton(frame_data, frame_number):
    frame_number = frame_number + 1
    plt.figure(figsize=(8, 6))
    
    # Plot each joint
    for column in columns:
        x, y = frame_data[column][:2]  # Obtener solo x e y, ignorar el score
        plt.scatter(x, y, label=column)
    
    # Conectar las articulaciones con líneas
    connections = [
        ('left_shoulder', 'right_shoulder'),
        ('left_shoulder', 'left_elbow'),
        ('left_elbow', 'left_wrist'),
        ('right_shoulder', 'right_elbow'),
        ('right_elbow', 'right_wrist'),
        ('left_shoulder', 'left_hip'),
        ('right_shoulder', 'right_hip'),
        ('left_hip', 'right_hip'),
        ('left_hip', 'left_knee'),
        ('left_knee', 'left_ankle'),
        ('right_hip', 'right_knee'),
        ('right_knee', 'right_ankle'),
        ('nose', 'mid_shoulder'),
        ('mid_shoulder', 'left_shoulder'),
        ('mid_shoulder', 'right_shoulder'),
        ('mid_shoulder', 'mid_hip'),
        ('mid_hip', 'left_hip'),
        ('mid_hip', 'right_hip')
    ]

    for joint1, joint2 in connections:
        x1, y1 = frame_data[joint1][:2]
        x2, y2 = frame_data[joint2][:2]
        plt.plot([x1, x2], [y1, y2], 'k-')

    plt.title(f'Gráfico de Articulaciones - Frame {frame_number}')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.gca().invert_yaxis()  # Invertir el eje Y para que el origen esté en la esquina superior izquierda
    plt.legend()

    # Guardar la imagen en el directorio especificado
    output_path = os.path.join(output_dir, f'frame_{frame_number:04d}.png')
    plt.savefig(output_path)
    plt.close()

# Graficar y guardar el "mono de palitos" para cada frame
for i in range(len(data)):
    plot_skeleton(data.loc[i], i)