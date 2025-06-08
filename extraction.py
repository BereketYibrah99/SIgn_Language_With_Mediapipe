import os

# Source and destination directories
source_dir = '/Users/bereket/Desktop/Python/landmarkProj/dataHunaga18'
destination_dir = '1/'

# Create destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

i = 1  # Start with 1 to match the example

# Loop through files in the source directory
for file in os.listdir(source_dir):
    # Check if the current item is a directory
    if os.path.isdir(os.path.join(source_dir, file)):
        for image in os.listdir(os.path.join(source_dir, file)):
            # Construct full path for the current image
            old_file_path = os.path.join(source_dir, file, image)
            
            # Construct new filename with incremented index
            new_file_name = f'hkjujhhgtfvgcrfgcrdfgvuhujhuhjhmnhgygty{i}.jpg'
            new_file_path = os.path.join(destination_dir, new_file_name)
            
            # Rename (move) the file to the destination directory
            os.rename(old_file_path, new_file_path)
            
            # Increment the index
            i += 1

print("Renaming and moving completed.")
