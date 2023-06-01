import cv2
import numpy as np

cap = cv2.VideoCapture('G:/Proj Curreent/Productize Tech/AI Engineer - ProductizeTech Assignment/task_2_video.mp4')

#HSV colours
green_lower = np.array([40, 50, 50])  
green_upper = np.array([80, 255, 255]) 

#for output
output_path = 'G:/Proj Curreent/Productize Tech/Task_2/task_2_video.mp4'
fps = 30
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for green color
    mask = cv2.inRange(hsv, green_lower, green_upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Mark green balls with red dots
    for contour in contours:
        (x, y), radius = cv2.minEnclosingCircle(contour)
        out.write(frame)
        
        # Filter out small contours (to remove noise)
        if radius > 5:
            # Draw a red dot at the center of the contour
            cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if ret and frame.shape[0] > 0 and frame.shape[1] > 0:
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Invalid frame size or unable to read the frame.")


out.release()

cap.release()
cv2.destroyAllWindows()
