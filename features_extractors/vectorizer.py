import os.path
import os
import numpy as np
import math
import pandas as pd
from matplotlib import pyplot as my_plot
import csv
import ast


def midscaculators(left_x, right_x, left_y, right_y):
    mid = np.array([((left_x + right_x) / 2), ((left_y + right_y) / 2)])
    return mid

def anglescalculators(x1, y1, x2, y2):
    degrees = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return degrees

def anglescalculaatorsthreepoints(a1, a2, b1, b2, c1, c2):
    degrees = math.degrees(math.atan2(c2 - b2, c1 - b1) - math.atan2(a2 - b2, a1 - b1))
    return degrees + 360 if degrees < 0 else degrees

class Vectorizer:
    def __init__(self, output_path):
        self.finalCsv = []
        self.finalcsvAngles = []
        self.dict_kp = {
            "nose": np.array([]),
            "left_shoulder": np.array([]),
            "right_shoulder": np.array([]),
            "left_elbow": np.array([]),
            "right_elbow": np.array([]),
            "left_wrist": np.array([]),
            "right_wrist": np.array([]),
            "left_hip": np.array([]),
            "right_hip": np.array([]),
            "left_knee": np.array([]),
            "right_knee": np.array([]),
            "left_ankle": np.array([]),
            "right_ankle": np.array([]),
            "mid_shoulder": np.array([]),
            "mid_hip": np.array([])
        }
        self.dict_angles = {
            "nose-mid_shoulder": np.array([]),
            "left_shoulder-left_elbow": np.array([]),
            "right_shoulder-right_elbow": np.array([]),
            "left_elbow-left_wrist": np.array([]),
            "right_elbow-right_wrist": np.array([]),
            "mid_shoulder-mid_hip": np.array([]),
            "left_hip-left_knee": np.array([]),
            "right_hip-right_knee": np.array([]),
            "left_knee-left_ankle": np.array([]),
            "right_knee-right_ankle": np.array([]),
            "mid_shoulder_angle": np.array([]),
            "left_shoulder_angle": np.array([]),
            "right_shoulder_angle": np.array([]),
            "left_elbow_angle": np.array([]),
            "right_elbow_angle": np.array([]),
            "left_hip_angle": np.array([]),
            "right_hip_angle": np.array([]),
            "left_knee_angle": np.array([]),
            "right_knee_angle": np.array([]),
        }
        self.frames = 0
        self.output_path = output_path

    def vectorizer(self, vectors):
        self.frames += 1
        print("KP frame: ", self.frames)
        self.dict_kp["nose"] = np.append(self.dict_kp["nose"], vectors[0])
        self.dict_kp["left_shoulder"] = np.append(self.dict_kp["left_shoulder"], vectors[5])
        self.dict_kp["right_shoulder"] = np.append(self.dict_kp["right_shoulder"], vectors[6])
        self.dict_kp["left_elbow"] = np.append(self.dict_kp["left_elbow"], vectors[7])
        self.dict_kp["right_elbow"] = np.append(self.dict_kp["right_elbow"], vectors[8])
        self.dict_kp["left_wrist"] = np.append(self.dict_kp["left_wrist"], vectors[9])
        self.dict_kp["right_wrist"] = np.append(self.dict_kp["right_wrist"], vectors[10])
        self.dict_kp["left_hip"] = np.append(self.dict_kp["left_hip"], vectors[11])
        self.dict_kp["right_hip"] = np.append(self.dict_kp["right_hip"], vectors[12])
        self.dict_kp["left_knee"] = np.append(self.dict_kp["left_knee"], vectors[13])
        self.dict_kp["right_knee"] = np.append(self.dict_kp["right_knee"], vectors[14])
        self.dict_kp["left_ankle"] = np.append(self.dict_kp["left_ankle"], vectors[15])
        self.dict_kp["right_ankle"] = np.append(self.dict_kp["right_ankle"], vectors[16])
        self.dict_kp["mid_shoulder"] = np.append(self.dict_kp["mid_shoulder"], np.array([
            midscaculators(vectors[5][0], vectors[6][0], vectors[5][1], vectors[6][1])]))
        self.dict_kp["mid_hip"] = np.append(self.dict_kp["mid_hip"], np.array([
            midscaculators(vectors[11][0], vectors[12][0], vectors[11][1], vectors[12][1])]))
        
        
     

    def keypoints_csv_generator(self):
        
        for key in self.dict_kp:
            if key != "mid_shoulder" and key != "mid_hip":
                self.dict_kp[key] = np.reshape(self.dict_kp[key], (self.frames, 3))
            else:
                self.dict_kp[key] = np.reshape(self.dict_kp[key], (self.frames, 2))
    

        for key in self.dict_kp:
            if not os.path.exists("csvs/keypoints/" + self.output_path):
                os.makedirs("csvs/keypoints/" + self.output_path)
            np.savetxt("csvs/keypoints/" + self.output_path + "/" + key + ".csv", self.dict_kp[key], delimiter=",")
        
        frame_data = {'etiqueta':'', 'frame':'', 'nose':'', 'left_shoulder':'', 'right_shoulder':'', 'left_elbow':'', 'right_elbow':'', 'left_wrist':'', 'right_wrist':'', 'left_hip':'', 'right_hip':'', 'left_knee':'', 'right_knee':'', 'left_ankle':'', 'right_ankle':'', 'mid_shoulder':'', 'mid_hip':''}

        for key in self.dict_kp:
            self.dict_kp[key] = np.array(self.dict_kp[key])
            

        for i in range(self.frames):
            frame_data['etiqueta'] = self.output_path
            frame_data['frame']=(i+1)
            frame_data['nose']=(self.dict_kp["nose"][i].tolist())
            frame_data['left_shoulder']=(self.dict_kp["left_shoulder"][i].tolist())
            frame_data['right_shoulder']=(self.dict_kp["right_shoulder"][i].tolist())
            frame_data['left_elbow']=(self.dict_kp["left_elbow"][i].tolist())
            frame_data['right_elbow']=(self.dict_kp["right_elbow"][i].tolist())
            frame_data['left_wrist']=(self.dict_kp["left_wrist"][i].tolist())
            frame_data['right_wrist']=(self.dict_kp["right_wrist"][i].tolist())
            frame_data['left_hip']=(self.dict_kp["left_hip"][i].tolist())
            frame_data['right_hip']=(self.dict_kp["right_hip"][i].tolist())
            frame_data['left_knee']=(self.dict_kp["left_knee"][i].tolist())
            frame_data['right_knee']=(self.dict_kp["right_knee"][i].tolist())
            frame_data['left_ankle']=(self.dict_kp["left_ankle"][i].tolist())
            frame_data['right_ankle']=(self.dict_kp["right_ankle"][i].tolist())
            frame_data['mid_shoulder']=(self.dict_kp["mid_shoulder"][i].tolist())
            frame_data['mid_hip']=(self.dict_kp["mid_hip"][i].tolist())
            self.finalCsv.append(frame_data)
            frame_data = {'etiqueta':'', 'frame':'', 'nose':'', 'left_shoulder':'', 'right_shoulder':'', 'left_elbow':'', 'right_elbow':'', 'left_wrist':'', 'right_wrist':'', 'left_hip':'', 'right_hip':'', 'left_knee':'', 'right_knee':'', 'left_ankle':'', 'right_ankle':'', 'mid_shoulder':'', 'mid_hip':''}


        df = pd.DataFrame(self.finalCsv)
        df.to_csv('csvs/keypoints/' + self.output_path + '/' + 'final_keypoints' + '.csv', index=False,mode='w+')


    def angles_csv_generator(self):
        for i in range(self.frames):
            self.dict_angles["nose-mid_shoulder"] = np.append(self.dict_angles["nose-mid_shoulder"], anglescalculators(
                self.dict_kp["nose"][i][0], self.dict_kp["nose"][i][1], self.dict_kp["mid_shoulder"][i][0], self.dict_kp["mid_shoulder"][i][1]))
            self.dict_angles["mid_shoulder-mid_hip"] = np.append(self.dict_angles["mid_shoulder-mid_hip"], anglescalculators(
                self.dict_kp["mid_shoulder"][i][0], self.dict_kp["mid_shoulder"][i][1], self.dict_kp["mid_hip"][i][0], self.dict_kp["mid_hip"][i][1]))
            self.dict_angles["left_shoulder-left_elbow"] = np.append(self.dict_angles["left_shoulder-left_elbow"], anglescalculators(
                self.dict_kp["left_shoulder"][i][0], self.dict_kp["left_shoulder"][i][1], self.dict_kp["left_elbow"][i][0], self.dict_kp["left_elbow"][i][1]))
            self.dict_angles["left_elbow-left_wrist"] = np.append(self.dict_angles["left_elbow-left_wrist"], anglescalculators(
                self.dict_kp["left_elbow"][i][0], self.dict_kp["left_elbow"][i][1], self.dict_kp["left_wrist"][i][0], self.dict_kp["left_wrist"][i][1]))
            self.dict_angles["right_shoulder-right_elbow"] = np.append(self.dict_angles["right_shoulder-right_elbow"], anglescalculators(
                self.dict_kp["right_shoulder"][i][0], self.dict_kp["right_shoulder"][i][1], self.dict_kp["right_elbow"][i][0], self.dict_kp["right_elbow"][i][1]))
            self.dict_angles["right_elbow-right_wrist"] = np.append(self.dict_angles["right_elbow-right_wrist"], anglescalculators(
                self.dict_kp["right_elbow"][i][0], self.dict_kp["right_elbow"][i][1], self.dict_kp["right_wrist"][i][0], self.dict_kp["right_wrist"][i][1]))
            self.dict_angles["left_hip-left_knee"] = np.append(self.dict_angles["left_hip-left_knee"], anglescalculators(
                self.dict_kp["left_hip"][i][0], self.dict_kp["left_hip"][i][1], self.dict_kp["left_knee"][i][0], self.dict_kp["left_knee"][i][1]))
            self.dict_angles["left_knee-left_ankle"] = np.append(self.dict_angles["left_knee-left_ankle"], anglescalculators(
                self.dict_kp["left_knee"][i][0], self.dict_kp["left_knee"][i][1], self.dict_kp["left_ankle"][i][0], self.dict_kp["left_ankle"][i][1]))
            self.dict_angles["right_hip-right_knee"] = np.append(self.dict_angles["right_hip-right_knee"], anglescalculators(
                self.dict_kp["right_hip"][i][0], self.dict_kp["right_hip"][i][1], self.dict_kp["right_knee"][i][0], self.dict_kp["right_knee"][i][1]))
            self.dict_angles["right_knee-right_ankle"] = np.append(self.dict_angles["right_knee-right_ankle"], anglescalculators(
                self.dict_kp["right_knee"][i][0], self.dict_kp["right_knee"][i][1], self.dict_kp["right_ankle"][i][0], self.dict_kp["right_ankle"][i][1]))
            self.dict_angles["mid_shoulder_angle"] = np.append(self.dict_angles["mid_shoulder_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["nose"][i][0], self.dict_kp["nose"][i][1], self.dict_kp["mid_shoulder"][i][0], self.dict_kp["mid_shoulder"][i][1],
                self.dict_kp["mid_hip"][i][0], self.dict_kp["mid_hip"][i][1]))
            self.dict_angles["left_shoulder_angle"] = np.append(self.dict_angles["left_shoulder_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["mid_shoulder"][i][0], self.dict_kp["mid_shoulder"][i][1], self.dict_kp["left_shoulder"][i][0], self.dict_kp["left_shoulder"][i][1],
                self.dict_kp["left_elbow"][i][0], self.dict_kp["left_elbow"][i][1]))
            self.dict_angles["left_elbow_angle"] = np.append(self.dict_angles["left_elbow_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["left_shoulder"][i][0], self.dict_kp["left_shoulder"][i][1], self.dict_kp["left_elbow"][i][0], self.dict_kp["left_elbow"][i][1],
                self.dict_kp["left_wrist"][i][0], self.dict_kp["left_wrist"][i][1]))
            self.dict_angles["right_shoulder_angle"] = np.append(self.dict_angles["right_shoulder_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["mid_shoulder"][i][0], self.dict_kp["mid_shoulder"][i][1], self.dict_kp["right_shoulder"][i][0], self.dict_kp["right_shoulder"][i][1],
                self.dict_kp["right_elbow"][i][0], self.dict_kp["right_elbow"][i][1]))
            self.dict_angles["right_elbow_angle"] = np.append(self.dict_angles["right_elbow_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["right_shoulder"][i][0], self.dict_kp["right_shoulder"][i][1], self.dict_kp["right_elbow"][i][0], self.dict_kp["right_elbow"][i][1],
                self.dict_kp["right_wrist"][i][0], self.dict_kp["right_wrist"][i][1]))
            self.dict_angles["left_hip_angle"] = np.append(self.dict_angles["left_hip_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["mid_hip"][i][0], self.dict_kp["mid_hip"][i][1], self.dict_kp["left_hip"][i][0], self.dict_kp["left_hip"][i][1],
                self.dict_kp["left_knee"][i][0], self.dict_kp["left_knee"][i][1]))
            self.dict_angles["left_knee_angle"] = np.append(self.dict_angles["left_knee_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["left_hip"][i][0], self.dict_kp["left_hip"][i][1], self.dict_kp["left_knee"][i][0], self.dict_kp["left_knee"][i][1],
                self.dict_kp["left_ankle"][i][0], self.dict_kp["left_ankle"][i][1]))
            self.dict_angles["right_hip_angle"] = np.append(self.dict_angles["right_hip_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["mid_hip"][i][0], self.dict_kp["mid_hip"][i][1], self.dict_kp["right_hip"][i][0], self.dict_kp["right_hip"][i][1],
                self.dict_kp["right_knee"][i][0], self.dict_kp["right_knee"][i][1]))
            self.dict_angles["right_knee_angle"] = np.append(self.dict_angles["right_knee_angle"], anglescalculaatorsthreepoints(
                self.dict_kp["right_hip"][i][0], self.dict_kp["right_hip"][i][1], self.dict_kp["right_knee"][i][0], self.dict_kp["right_knee"][i][1],
                self.dict_kp["right_ankle"][i][0], self.dict_kp["right_ankle"][i][1]))

            

        for key in self.dict_angles:
            self.dict_angles[key] = np.reshape(self.dict_angles[key], (self.frames, 1))
        for key in self.dict_angles:
            if not os.path.exists("csvs/angles/" + self.output_path):
                os.makedirs("csvs/angles/" + self.output_path)
            np.savetxt("csvs/angles/" + self.output_path + "/" + key + ".csv", self.dict_angles[key], delimiter=",")
        
        frame_data = {'etiqueta':'',
                        'frame':'',
                        "nose-mid_shoulder":            '',
                        "mid_shoulder-mid_hip":        '',
                        "left_shoulder-left_elbow":     '',
                        "left_elbow-left_wrist":        '',
                        "right_shoulder-right_elbow":   '',
                        "right_elbow-right_wrist":      '',
                        "left_hip-left_knee":           '',
                        "left_knee-left_ankle":         '',
                        "right_hip-right_knee":         '',
                        "right_knee-right_ankle":       '',
                        "mid_shoulder_angle":           '',
                        "left_shoulder_angle":          '',
                        "left_elbow_angle":             '',
                        "right_shoulder_angle":         '',
                        "right_elbow_angle":            '',
                        "left_hip_angle":               '',
                        "left_knee_angle":              '',
                        "right_hip_angle":              '',
                        "right_knee_angle":         ''}
        
        for i in range(self.frames):
            frame_data['etiqueta'] = self.output_path
            frame_data['frame']=(i+1)
            frame_data['nose-mid_shoulder']=(self.dict_angles["nose-mid_shoulder"][i].tolist())
            frame_data['mid_shoulder-mid_hip']=(self.dict_angles["mid_shoulder-mid_hip"][i].tolist())
            frame_data['left_shoulder-left_elbow']=(self.dict_angles["left_shoulder-left_elbow"][i].tolist())
            frame_data['left_elbow-left_wrist']=(self.dict_angles["left_elbow-left_wrist"][i].tolist())
            frame_data['right_shoulder-right_elbow']=(self.dict_angles["right_shoulder-right_elbow"][i].tolist())
            frame_data['right_elbow-right_wrist']=(self.dict_angles["right_elbow-right_wrist"][i].tolist())
            frame_data['left_hip-left_knee']=(self.dict_angles["left_hip-left_knee"][i].tolist())
            frame_data['left_knee-left_ankle']=(self.dict_angles["left_knee-left_ankle"][i].tolist())
            frame_data['right_hip-right_knee']=(self.dict_angles["right_hip-right_knee"][i].tolist())
            frame_data['right_knee-right_ankle']=(self.dict_angles["right_knee-right_ankle"][i].tolist())
            frame_data['mid_shoulder_angle']=(self.dict_angles["mid_shoulder_angle"][i].tolist())
            frame_data['left_shoulder_angle']=(self.dict_angles["left_shoulder_angle"][i].tolist())
            frame_data['left_elbow_angle']=(self.dict_angles["left_elbow_angle"][i].tolist())
            frame_data['right_shoulder_angle']=(self.dict_angles["right_shoulder_angle"][i].tolist())
            frame_data['right_elbow_angle']=(self.dict_angles["right_elbow_angle"][i].tolist())
            frame_data['left_hip_angle']=(self.dict_angles["left_hip_angle"][i].tolist())
            frame_data['left_knee_angle']=(self.dict_angles["left_knee_angle"][i].tolist())
            frame_data['right_hip_angle']=(self.dict_angles["right_hip_angle"][i].tolist())
            frame_data['right_knee_angle']=(self.dict_angles["right_knee_angle"][i].tolist())
            
            self.finalcsvAngles.append(frame_data)
            frame_data = {'etiqueta':'',
                        'frame':'',
                        "frame":                        '',
                        "nose-mid_shoulder":            '',
                        "mid_shoulder-mid_hip":        '',
                        "left_shoulder-left_elbow":     '',
                        "left_elbow-left_wrist":        '',
                        "right_shoulder-right_elbow":   '',
                        "right_elbow-right_wrist":      '',
                        "left_hip-left_knee":           '',
                        "left_knee-left_ankle":         '',
                        "right_hip-right_knee":         '',
                        "right_knee-right_ankle":       '',
                        "mid_shoulder_angle":           '',
                        "left_shoulder_angle":          '',
                        "left_elbow_angle":             '',
                        "right_shoulder_angle":         '',
                        "right_elbow_angle":            '',
                        "left_hip_angle":               '',
                        "left_knee_angle":              '',
                        "right_hip_angle":              '',
                        "right_knee_angle":         ''}
            
            df = pd.DataFrame(self.finalcsvAngles)
            df.to_csv('csvs/angles/' + self.output_path + '/' + 'final_angles' + '.csv', index=False,mode='w+')
            
    
    
    def framesKeypointsToImanges(self):
        # Leer el archivo CSV

        csv_file_path = 'csvs/keypoints/' + self.output_path + '/' + 'final_keypoints' + '.csv'
        output_dir = 'csvs/keypoints/' + self.output_path + '/' + 'seriesTiempo'
        data = pd.read_csv(csv_file_path)

        # Crear el directorio si no existe
        os.makedirs(output_dir, exist_ok=True)

        # Convertir las cadenas de texto de las columnas en numpy arrays
        columns = ['nose', 'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 
                'right_wrist', 'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 
                'right_ankle', 'mid_shoulder', 'mid_hip']

        for column in columns:
            data[column] = data[column].apply(lambda x: np.array(ast.literal_eval(x)))

        # Dibujar el "mono de palitos" para cada frame y guardar la imagen
        def plot_skeleton(frame_data, frame_number):
            frame_number = frame_number + 1
            my_plot.figure(figsize=(8, 6))

            # Plot each joint
            for column in columns:
                x, y = frame_data[column][:2]  # Obtener solo x e y, ignorar el score
                my_plot.scatter(x, y, label=column)

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
                my_plot.plot([x1, x2], [y1, y2], 'k-')

            my_plot.title(f'Gráfico de Articulaciones - Frame {frame_number}')
            my_plot.xlabel('Coordenada X')
            my_plot.ylabel('Coordenada Y')
            my_plot.gca().invert_yaxis()  # Invertir el eje Y para que el origen esté en la esquina superior izquierda
            my_plot.legend()

            # Guardar la imagen en el directorio especificado
            output_path = os.path.join(output_dir, f'frame_{frame_number:04d}.png')
            my_plot.savefig(output_path)
            my_plot.close()

        # Graficar y guardar el "mono de palitos" para cada frame
        for i in range(len(data)):
            plot_skeleton(data.loc[i], i)

    print("Imágenes de monitos de palitos guardadas en el directorio especificado.")

    def plotter(self):
        for key in self.dict_angles:
            x = np.arange(0, self.frames)
            y = self.dict_angles[key]
            my_plot.figure()
            my_plot.title(key)
            my_plot.xlabel("Frames")
            my_plot.ylabel("Angles")
            my_plot.plot(x, y, color="blue")
            if not os.path.exists("plots/" + self.output_path):
                os.makedirs("plots/" + self.output_path)
            my_plot.savefig("plots/" + self.output_path + "/" + key + ".png")
            

