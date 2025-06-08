import cv2
import os

# Define input and output folders
input_folder = '/Users/bereket/Desktop/Python/landmarkProj/data00000000333/0'   # Replace with your input folder path
output_folder = 'mlmknjbyhbybhb/'      # Replace with your output folder path

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all image files in the input folder (you can add more extensions if needed)
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Process each image
for index, image_file in enumerate(image_files, start=1):
    # Construct full path to the image
    input_image_path = os.path.join(input_folder, image_file)

    # Read the image
    image = cv2.imread(input_image_path)

    # Check if the image is loaded successfully
    if image is None:
        print(f"Error: Image {image_file} not found or cannot be loaded.")
        continue

    # Save the original image with an ordered filename
    original_output_path = os.path.join(output_folder, f'akkkkkoriginal_{index}.jpg')  # Change extension if needed
    cv2.imwrite(original_output_path, image)

    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)

    # Save the flipped image with an ordered filename
    flipped_output_path = os.path.join(output_folder, f'aakkkhytftvtfcfcdcdcdckk{index}.jpg')   # Change extension if needed
    cv2.imwrite(flipped_output_path, flipped_image)

    print(f"Processed {image_file}: saved as {original_output_path} and {flipped_output_path}")
