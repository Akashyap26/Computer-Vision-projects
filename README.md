# Computer-Vision-projects
GitHub folder containing a computer vision project code and resources for image analysis, object detection, and visual recognition.


1. Task 1: Automatic Object Outline/Border Detection Develop a basic OpenCV Python script that draws an object’s outline
using rembg library & OpenCV Image processing.

a. In the Python script add a variable to specify the input
image path.
b. The script should read the image & display it.
c. Ask the user to draw a rectangle over an object inside the
image. (cv2.selectROI)
d. Crop the selected Region Of Interest (ROI) and pass it to
rembg library. (https://github.com/danielgatis/rembg) [pip
install rembg]
e. The library will remove the background from the ROI and
return the image back.
f. Draw an outline over the object since it doesn’t have any
background now.g. Overlay the object outline in the original input image and
show it as output.
h. Allow the user to do this again and again until “q” is
pressed.
i. To clear the outline, allow the user to press “c”
Submission -
j. Screen record using Loom/OBS/Any Other Software and
run your script on “1.jpg” & “2.jpg” in the “TEST IMAGES”
folder.
k. Draw a box over the women in red pants for “1.jpg”
l. Draw a box over the car for “2.jpg”


2. Task 2: Draw Red Dot On Green Polka Dots (Development) 

a. The input video for this task is “task_2_video.mp4”
b. In this task, detect the green polka dots in the video. (HSV
filtering)
c. You can hardcode the HSV range values for the green color.
d. Draw a red dot at the center of each green polka dot.
e. Do this for all the frames in the video and generate an
output video.
f. You can consider both the green dots (Dark & Light) or any
one of them.
g. You can keep the size of the red dot the same for all the
green dots.
h. Output example of a single frame -i. Write an algorithm to output such red dots drawn at the
center of the green dots.
j. If 2 green dots overlap, you can draw a single red dot or 2
whichever you feel is easier for you.


3. Task 3: EasyOCR (Development) 

a. For this task, use the EasyOCR library in Python.
b. Write a program in Python OpenCV to read all the image
files in a folder.
c. For each file, run the EasyOCR library and store all the
output images in a folder
d. Input images will look like “task_3_input.jpg”
e. The output image should look like
“task_3_partial_output.png” but in place of red boxes with
numbers, it should be red boxes with green-colored OCR
detected text beside it. Example is given for “DOB
03/05/1960” in the “task_3_partial_output.png”
f. Develop this algorithm and run it on all the images inside
“License Images.zip”.
g. Store all the output images in a folder named “License
Outputs” and upload the folder to your submission drivefolder. Do not zip the “License Outputs” folder. The images
should be viewable directly on Google Drive.
h. Upload your .py file to your Google Drive folder.


4. Task 4: MediaPipe Pose Estimation (Inference)

a. The input video for this task is “task_4_video.mp4”
b. Draw the person’s skeleton in the video using
MediaPipe Library
c. This task is just to check if you’re able to use MediaPipe
pose estimation for inference.
d. This is a pose estimation task and not face key point
detection.
