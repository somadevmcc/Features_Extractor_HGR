from threading import Thread
from time import perf_counter
from detectron2.detectron import Detectron
from DensePose.dense import Dense
from database import Conexiones as con

import os
def main():
    for videos in os.listdir("video-inputs"):
        video_path = "video-inputs/" + videos
        name = videos.split(".")[0]

        obj_det = Detectron(video_path, name)
        obj_den = Dense(video_path, name)
        
        start_time = perf_counter()
        obj_det.videoSkeleton()
        obj_den.videoMask()
        


        end_time = perf_counter()

        print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
    
    # for videos in os.listdir("video-inputs"):
    #     video_path = "video-inputs/" + videos
    #     name = videos.split(".")[0]

    #     obj_det = Detectron(video_path, name)
    #     obj_den = Dense(video_path, name)

    #     t1 = Thread(target=obj_det.videoSkeleton)
    #     t2 = Thread(target=obj_den.videoMask)

    #     start_time = perf_counter()

    #     t1.start()
    #     t2.start()

    #     t1.join()
    #     t2.join()

    #     end_time = perf_counter()

    #     print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
  

if __name__ == "__main__":
    main()
