import os.path

import numpy as np
import math
from matplotlib import pyplot as my_plot
import csv

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
        
        
        frame_data = {
            "etiqueta": self.output_path,
            "frame": self.frames,
            "nose": np.append(self.dict_kp["nose"], vectors[0]).tolist(),
            "left_shoulder": np.append(self.dict_kp["left_shoulder"], vectors[5]).tolist(),
            "right_shoulder": np.append(self.dict_kp["left_shoulder"], vectors[6]).tolist(),
            "left_elbow": np.append(self.dict_kp["left_shoulder"], vectors[7]).tolist(),
            "right_elbow": np.append(self.dict_kp["left_shoulder"], vectors[8]).tolist(),
            "left_wrist": np.append(self.dict_kp["left_shoulder"], vectors[9]).tolist(),
            "right_wrist": np.append(self.dict_kp["left_shoulder"], vectors[10]).tolist(),
            "left_hip": np.append(self.dict_kp["left_shoulder"], vectors[11]).tolist(),
            "right_hip": np.append(self.dict_kp["left_shoulder"], vectors[12]).tolist(),
            "left_knee": np.append(self.dict_kp["left_shoulder"], vectors[13]).tolist(),
            "right_knee": np.append(self.dict_kp["left_shoulder"], vectors[14]).tolist(),
            "left_ankle": np.append(self.dict_kp["left_shoulder"], vectors[15]).tolist(),
            "right_ankle": np.append(self.dict_kp["left_shoulder"], vectors[16]).tolist(),
            "mid_shoulder": np.append(self.dict_kp["mid_shoulder"], np.array([
            midscaculators(vectors[5][0], vectors[6][0], vectors[5][1], vectors[6][1])])).tolist(),
            "mid_hip":  np.append(self.dict_kp["mid_hip"], np.array([
            midscaculators(vectors[11][0], vectors[12][0], vectors[11][1], vectors[12][1])])).tolist()
        }
        self.finalCsv.append(frame_data)


    def keypoints_csv_generator(self):
        frame_data = {}
        for key in self.dict_kp:
            if key != "mid_shoulder" and key != "mid_hip":
                self.dict_kp[key] = np.reshape(self.dict_kp[key], (self.frames, 3))
            else:
                self.dict_kp[key] = np.reshape(self.dict_kp[key], (self.frames, 2))
        print(self.dict_kp['nose'])

        for key in self.dict_kp:
            for i in range(self.frames):
                frame_data['etiqueta'].append(self.output_path)
                frame_data['frame'].append(i+1)
                frame_data[key][i].append(self.dict_kp[key][i].tolist())

        for key in self.dict_kp:
            if not os.path.exists("csvs/keypoints/" + self.output_path):
                os.makedirs("csvs/keypoints/" + self.output_path)
            np.savetxt("csvs/keypoints/" + self.output_path + "/" + key + ".csv", self.dict_kp[key], delimiter=",")
        
        keys = self.finalCsv[0].keys()
        if not os.path.exists("csvs/keypoints/" + self.output_path):
            os.makedirs("csvs/keypoints/" + self.output_path)

        with open("csvs/keypoints/" + self.output_path + "/final_keypoints.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for data in self.frame_data:
                writer.writerow(data)

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

            frame_data = {
                "etiqueta": self.output_path,
                "frame": (i+1),
                "nose-mid_shoulder": self.dict_angles["nose-mid_shoulder"],
                "mid_shoulder-mid_hip": self.dict_angles["mid_shoulder-mid_hip"],
                "left_shoulder-left_elbow": self.dict_angles["left_shoulder-left_elbow"],
                "left_elbow-left_wrist": self.dict_angles["left_elbow-left_wrist"],
                "right_shoulder-right_elbow": self.dict_angles["right_shoulder-right_elbow"],
                "right_elbow-right_wrist": self.dict_angles["right_elbow-right_wrist"],
                "left_hip-left_knee": self.dict_angles["left_hip-left_knee"],
                "left_knee-left_ankle": self.dict_angles["left_knee-left_ankle"],
                "right_hip-right_knee": self.dict_angles["right_hip-right_knee"],
                "right_knee-right_ankle": self.dict_angles["right_knee-right_ankle"],
                "mid_shoulder_angle": self.dict_angles["mid_shoulder_angle"],
                "left_shoulder_angle": self.dict_angles["left_shoulder_angle"],
                "left_elbow_angle": self.dict_angles["left_elbow_angle"],
                "right_shoulder_angle": self.dict_angles["right_shoulder_angle"],
                "right_elbow_angle": self.dict_angles["right_elbow_angle"],
                "left_hip_angle": self.dict_angles["left_hip_angle"],
                "left_knee_angle": self.dict_angles["left_knee_angle"],
                "right_hip_angle": self.dict_angles["right_hip_angle"],
                "right_knee_angle": self.dict_angles["right_knee_angle"]
            }
            self.finalcsvAngles.append(frame_data)

        for key in self.dict_angles:
            self.dict_angles[key] = np.reshape(self.dict_angles[key], (self.frames, 1))
        for key in self.dict_angles:
            if not os.path.exists("csvs/angles/" + self.output_path):
                os.makedirs("csvs/angles/" + self.output_path)
            np.savetxt("csvs/angles/" + self.output_path + "/" + key + ".csv", self.dict_angles[key], delimiter=",")
        
        keys = self.finalcsvAngles[0].keys()
        if not os.path.exists("csvs/angles/" + self.output_path):
            os.makedirs("csvs/angles/" + self.output_path)
        with open("csvs/angles/" + self.output_path + "/final_angles.csv", "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for data in self.finalcsvAngles:
                writer.writerow(data)

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

