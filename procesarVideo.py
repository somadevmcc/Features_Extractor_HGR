import cv2
import numpy as np
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
import requests
def connect_to_db(list_of_tuples):
    conn = psycopg2.connect(
    dbname='mascaras',
    user='postgres.ihbjcyzyzkchmchmzpvv',
    password='Vt123mssih!!',
    host='aws-0-us-west-1.pooler.supabase.com',
    port='6543'
    )

    cur = conn.cursor()


    # Insert data into the table
    insert_query = '''
        INSERT INTO ctl_videomascaras (idu_etiqueta,frame,red, green, blue) VALUES (%s,%s,%s, %s, %s);
    '''

    execute_batch(cur, insert_query, list_of_tuples)

    # Commit and close
    conn.commit()
    cur.close()
    conn.close()

def video_to_frames(video_path, output_dir):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to numpy array
        #frame_array = np.array(frame)
        frame_array = frame.reshape(-1, frame.shape[2])  # Flatten the array
        list_of_tuples = [(14,frame_count,*map(int, row)) for row in frame_array]  # Convert to list of tuples with int
        
        print(list_of_tuples)
        connect_to_db(list_of_tuples)
        # Save numpy array as CSV
        output_path = f"{output_dir}/frame_{frame_count}.csv"
        pd.DataFrame(frame_array.reshape(-1, frame_array.shape[2])).to_csv(output_path, index=False, header=False)
        
        frame_count += 1
        break

    cap.release()

def load_frame_from_csv(csv_path):
    # Load CSV file into numpy array
    df = pd.read_csv(csv_path, header=None)
    # Reshape the array to the original frame shape
    frame_array = df.values.reshape(-1, 3)
    return frame_array

# Paths
video_path = 'C:\Users\luisf\Documents\GitHub\Features_Extractor_HGR\video-inputs\FERNANDO_01.mp4'
output_dir = 'video-outputs\FERNANDO_01'

# Convert video to frames and save as CSV
video_to_frames(video_path, output_dir)

# Load a specific frame from CSV
#csv_path = f"{output_dir}/frame_0.csv"
#frame_array = load_frame_from_csv(csv_path)

#print(frame_array)