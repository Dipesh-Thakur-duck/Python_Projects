#! /home/dipesh-thakur/Documents/python_projects/venv/bin/python

# WAP that walks through a folder tree and searches for exceptionally large files or folders - say, ones that have a file size of more than 100MB. Print these files with their absolute path to the screen.

import os

source = "/home/dipesh-thakur/"

for folderName, subfolders, filenames in os.walk(source):
    for filename in filenames:
        filepath = os.path.join(folderName,filename)
        try:
            if os.path.getsize(filepath) >= 104857600: # 100 MB
                print(filepath)
        except (FileNotFoundError, PermissionError):
            continue

# sometimes os.walk() will give a file but when you check the its size, the file has disappeared or become unreachable due to file chage during the walk