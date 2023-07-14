import os
import shutil

parent_folder = r"C:\Users\paula\Desktop\안민주\Sejong Data project\CODE\업로드\충청,전라,제주\라벨링(충천,전라,제주,세부발화)\people\talk\cc"  # Replace with the actual path to the parent folder

# Create a list to store the file paths
file_paths = []

# Iterate through subfolders
for root, dirs, files in os.walk(parent_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)  # Add file path to the list

# Move the files to the parent folder
for file_path in file_paths:
    shutil.move(file_path, parent_folder)

print("Files moved successfully!")
