import cv2
from cvzone.PoseModule import PoseDetector

def mascaraFrame(numFrame):
    # Define the path to the video file
    video_path = 'video-outputs\FERNANDO_01\mask.avi'

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video file opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        exit()
    # Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, numFrame)

    # Read the frame
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if ret:
        # Display the frame
        cap.release()
        return frame
    else:
        print(f"Error: Could not read frame {numFrame}")

    # Release the video capture object and close all OpenCV windows
    cap.release()



# Define the path to the video file
video_path = r'video-inputs\FERNANDO_01.mp4'
output_path = 'video-outputs/FERNANDO_01_cut.mp4'


# Initialize the PoseDetector
detector = PoseDetector()

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if video file opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Initialize the VideoWriter to save the new video
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Initialize variables to store the bounding box dimensions
rect_x, rect_y, rect_w, rect_h = 0, 0, 0, 0
Numframe = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Find the pose in the frame
    img = detector.findPose(frame, draw=False)
    
    # Get the list of landmarks
    lmList, _ = detector.findPosition(img, bboxWithHands=False)
    
    if lmList:
        # Calculate bounding box dimensions based on landmarks
        x_min = min(lmList, key=lambda x: x[0])[0]
        x_max = max(lmList, key=lambda x: x[0])[0]
        y_min = min(lmList, key=lambda x: x[1])[1]
        y_max = max(lmList, key=lambda x: x[1])[1]
        
        # Update rectangle dimensions
        rect_x = x_min
        rect_y = y_min
        rect_w = x_max - x_min
        rect_h = y_max - y_min
    
    # Ensure rectangle is within frame boundaries
    rect_x = max(0, rect_x)
    rect_y = max(0, rect_y)
    rect_w = min(width - rect_x, rect_w)
    rect_h = min(height - rect_y, rect_h)
    
    if rect_w > 0 and rect_h > 0:
        # Draw the rectangle on the frame
        cv2.rectangle(frame, (rect_x, rect_y), (rect_x + rect_w, rect_y + rect_h), (255, 0, 0), 2)
        
        # Crop the frame to the rectangle region
        
        maskFrame = mascaraFrame(Numframe)
        cropped_frame = maskFrame[rect_y:rect_y + rect_h, rect_x:rect_x + rect_w]
        cv2.imshow('Frame', maskFrame)
        if cropped_frame.size != 0:
            # Resize cropped frame back to original frame size
            resized_cropped_frame = cv2.resize(cropped_frame, (width, height))
            
            # Write the resized cropped frame to the output video
            out.write(resized_cropped_frame)
    
    # Display the frame with the pose and bounding box (for debugging purposes)
    #cv2.imshow('Frame', frame)
    Numframe += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects and close all OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
