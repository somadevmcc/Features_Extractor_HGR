import cv2

# Define the path to the video file
video_path = r'video-inputs\FERNANDO_01.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if video file opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()

# Total number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Specify the frame number you want to check (e.g., frame 100)
frame_number_to_check = 1

# Set the frame position
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number_to_check)

# Read the frame
ret, frame = cap.read()

# Check if the frame was read successfully
if ret:
    # Display the frame
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)
else:
    print(f"Error: Could not read frame {frame_number_to_check}")

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
