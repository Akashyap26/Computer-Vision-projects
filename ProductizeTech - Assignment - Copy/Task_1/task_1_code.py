import cv2
import rembg
image = cv2.imread(str(input()))

down_width = 1280
down_height = 720
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

x, y, w, h = cv2.selectROI(resized_down)
roi = resized_down[y:y+h, x:x+w]

# Convert ROI to bytes
roi_bytes = cv2.imencode('.png', roi)[1].tobytes()

# Remove background using Rembg
resul = rembg.remove(roi_bytes)
import numpy as np

# Convert result to numpy array
result = np.frombuffer(resul, dtype=np.uint8)

# Decode image from numpy array
result_img = cv2.imdecode(result, cv2.IMREAD_UNCHANGED)

# Find contours
gray = cv2.cvtColor(result_img, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Adjust contour coordinates based on ROI position
for contour in contours:
    contour[:, 0, 0] += x  # Add x-coordinate of ROI
    contour[:, 0, 1] += y  # Add y-coordinate of ROI

# Draw contours on the original image
fin = cv2.drawContours(resized_down, contours, -1, (0, 255, 0), 2)
cv2.imshow('Modified Image', fin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the modified image
#cv2.imwrite('G:\Proj Curreent\Productize Tech\Task_1\image.jpg', fin)

