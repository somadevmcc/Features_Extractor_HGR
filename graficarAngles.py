import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
import os

# Ruta del archivo CSV (usar r antes de la cadena o dobles barras invertidas)
csv_file_path = r'C:\Users\luisf\Documents\GitHub\Features_Extractor_HGR\csvs\angles\fernando1\final_angles.csv'

# Ruta del directorio donde se guardarán las imágenes
output_dir = r'C:\Users\luisf\Documents\GitHub\Features_Extractor_HGR\csvs\angles\fernando1\seriesTiempo'

# Crear el directorio si no existe
os.makedirs(output_dir, exist_ok=True)

# Leer el archivo CSV
data = pd.read_csv(csv_file_path)
# Convertir las cadenas de texto de las columnas en numpy arrays
columns = ['nose-mid_shoulder', 'mid_shoulder-mid_hip', 'left_shoulder-left_elbow', 'left_elbow-left_wrist', 
           'right_shoulder-right_elbow', 'right_elbow-right_wrist', 'left_hip-left_knee', 'left_knee-left_ankle', 
           'right_hip-right_knee', 'right_knee-right_ankle', 'mid_shoulder_angle', 'left_shoulder_angle', 
           'left_elbow_angle', 'right_shoulder_angle', 'right_elbow_angle', 'left_hip_angle', 'left_knee_angle', 
           'right_hip_angle', 'right_knee_angle']

def safe_literal_eval(val):
    try:
        return np.array(ast.literal_eval(val))
    except (ValueError, SyntaxError):
        return np.nan

for column in columns:
    data[column] = data[column].apply(lambda x: safe_literal_eval(x) if pd.notnull(x) else np.nan)

# Función para calcular las posiciones 2D de las articulaciones del monito
def calculate_joint_positions(angles):
     # Inicializa las posiciones del monito (x, y)
    positions = {
        'mid_shoulder': (0, 0),
        'nose': (0, -1),
        'mid_hip': (0, 1),
        'left_shoulder': (0, -1),  # Añadir otras articulaciones con posiciones iniciales si es necesario
        'left_elbow': (0, -2),
        'left_wrist': (0, -3),
        'right_shoulder': (0, -1),
        'right_elbow': (0, -2),
        'right_wrist': (0, -3),
        'left_hip': (0, 1),
        'left_knee': (0, 2),
        'left_ankle': (0, 3),
        'right_hip': (0, 1),
        'right_knee': (0, 2),
        'right_ankle': (0, 3)
    }

    # Longitudes de las partes del cuerpo (arbitrarias, ajusta según sea necesario)
    lengths = {
        'nose-mid_shoulder': 1,
        'mid_shoulder-mid_hip': 1,
        'left_shoulder-left_elbow': 1,
        'left_elbow-left_wrist': 1,
        'right_shoulder-right_elbow': 1,
        'right_elbow-right_wrist': 1,
        'left_hip-left_knee': 1,
        'left_knee-left_ankle': 1,
        'right_hip-right_knee': 1,
        'right_knee-right_ankle': 1,
    }

    # Convertir los ángulos a radianes y calcular las posiciones de las articulaciones
    for part, angle_list in angles.items():
        if isinstance(angle_list, list) and len(angle_list) > 0:  # Verificar si angle_list es una lista no vacía
            angle = np.deg2rad(angle_list[0])  # Convertir el ángulo a radianes
            joint1, joint2 = part.split('-')
            x, y = positions[joint1]
            length = lengths[part]
            positions[joint2] = (x + length * np.cos(angle), y + length * np.sin(angle))


    return positions

# Función para graficar al monito de palitos
def plot_stick_figure(positions, frame_number):
    plt.figure(figsize=(6, 6))
    
    # Dibuja las líneas entre las articulaciones
    plt.plot([positions['nose'][0], positions['mid_shoulder'][0]], [positions['nose'][1], positions['mid_shoulder'][1]], 'k-')
    plt.plot([positions['mid_shoulder'][0], positions['mid_hip'][0]], [positions['mid_shoulder'][1], positions['mid_hip'][1]], 'k-')

    # Dibuja las extremidades
    for joint1, joint2 in [('left_shoulder', 'left_elbow'), ('left_elbow', 'left_wrist'),
                           ('right_shoulder', 'right_elbow'), ('right_elbow', 'right_wrist'),
                           ('left_hip', 'left_knee'), ('left_knee', 'left_ankle'),
                           ('right_hip', 'right_knee'), ('right_knee', 'right_ankle')]:
        plt.plot([positions[joint1][0], positions[joint2][0]], [positions[joint1][1], positions[joint2][1]], 'k-')

    # Configura la gráfica
    plt.title(f'Monito de Palitos - Frame {frame_number}')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)

    # Guardar la imagen en el directorio especificado
    output_path = os.path.join(output_dir, f'stick_figure_frame_{frame_number:04d}.png')
    plt.savefig(output_path)
    plt.close()

# Procesar y graficar cada frame
for idx, row in data.iterrows():
    angles = {col: row[col][0] for col in columns if pd.notnull(row[col])}
    positions = calculate_joint_positions(angles)
    plot_stick_figure(positions, row['frame'])

print("Imágenes de monitos de palitos guardadas en el directorio especificado.")