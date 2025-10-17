#! /home/dipesh-thakur/Documents/python_projects/venv/bin/python

# WAP a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.


import os, shutil

source = os.path.abspath('./Regex_Search')
number = 1
while True:
    destination = os.path.join(os.path.abspath('./'), f'selective_copy_{number}')
    if not os.path.exists(destination):
        break
    number = number + 1
    
print(f'Creating {destination}....')
os.makedirs(destination)

# Ask for the file extension
extension = input("Enter the file extension you want copied (e.g: .zip): ")

# Walk through the folder tree
for folderName, subfolders, filenames in os.walk(source):

    for filename in filenames:
        if filename.endswith(extension):
            # Get full source and destination paths
            source_path = os.path.join(folderName, filename)
            dest_path = os.path.join(destination, filename)
            # Copy the file
            shutil.copy(source_path, dest_path)
            print(f"Copied: {filename}")

print(f"\n All {extension} files have been copied to: {destination}")