import os
import hashlib
from PIL import Image

def deduplicate(dir_path):
    # Create a dictionary to store the file paths and their corresponding
    # hash values
    files = {}

    # Walk through the directory and calculate the hash value for each file
    for root, dirs, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)

            # Check if the file is a photo (JPEG or PNG)
            if file_path.endswith(('.jpg', '.jpeg', '.png')):
                # Calculate the perceptual hash value for the photo
                image = Image.open(file_path)
                hash_value = imagehash.phash(image)

                # If the hash value is already in the dictionary, it means we have
                # found a duplicate photo. In this case, we can remove the file.
                if hash_value in files:
                    #os.remove(file_path)
                    print("Duplicate found")
                else:
                    files[hash_value] = file_path

    # Print the list of unique photos
    for file_path in files.values():
        print(file_path)

# Use the deduplicate function to deduplicate the photos in the current
# directory
deduplicate(os.getcwd())

