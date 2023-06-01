import cv2
import easyocr
import os

def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'],gpu=True)

    # Iterate over the image files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Read the image using OpenCV
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)

            # Perform text recognition using EasyOCR
            results = reader.readtext(image)

            # Draw text above the detected regions
            for (text, bbox, _) in results:
                if len(bbox) == 4:
                    x, y, w, h = bbox
                elif len(bbox) == 2:
                    (x, y), (w, h) = bbox
                else:
                    continue

                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Save the modified image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, image)

    print("Processing completed. Output images are saved in the 'License Outputs' folder.")


inf = "G:/Proj Curreent/Productize Tech/AI Engineer - ProductizeTech Assignment/License Images"
outf = 'G:\Proj Curreent\Productize Tech\Task_3\Output'

# Process images and store the output
process_images(inf, outf)
