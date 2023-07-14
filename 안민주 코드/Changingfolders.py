import os
import shutil

source_folder = r"C:\Users\paula\Desktop\안민주\Sejong Data project\CODE\업로드\충청,전라,제주\라벨링(충천,전라,제주,세부발화)\person\say\cc"  # Replace with the path to the source folder
destination_folder = r"C:\Users\paula\Desktop\FINAL DATA\충청\say"  # Replace with the path to the destination folder

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate through the files and subdirectories in the source folder
for item in os.listdir(source_folder):
    item_path = os.path.join(source_folder, item)
    destination_path = os.path.join(destination_folder, item)

    # Copy the item to the destination folder
    shutil.copy(item_path, destination_path)

print("Contents moved successfully!")