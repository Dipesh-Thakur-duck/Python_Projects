#! /home/dipesh-thakur/Documents/python_projects/venv/bin/python

# WAP that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

import os, shutil, re

pattern = re.compile(r'(\D+)(\d+)(\.\w+)$')

# This matches:

# Prefix (\D+) — non-digit characters, like "spam"

# Number (\d+) — digits like "001"

# Extension (.\w+) — like ".txt"

source = os.path.join(os.path.abspath("./"),'Regex_Search')

files_in_folder = list(filter(lambda x: not os.path.isdir(os.path.join(source,x)),os.listdir(source)))

input_files = []
for file in files_in_folder:
    if pattern.match(file):
        input_files.append(file)
input_files.sort()

pattern_1 = re.compile(r'(\d+)')

numbers = []
for file in input_files:
    mo = pattern_1.search(file)
    if mo:
        numbers.append(mo.group(1))

count = 0
replace = {}
expected = int(numbers[0])
for num in numbers:
    actual = int(num)
    if actual != expected:
        replace[num] = str(expected)
    expected += 1

new_files = {}

for file in input_files: 
    pattern = re.compile(r'(\d+)')
    new_name = pattern.sub(lambda m: replace.get(m.group(1), m.group(1)), file)
    if new_name != file:
        new_files[file] = new_name


# pattern.sub(pattern,repl, string)
# repl -> either a string or function
# when repl is function -> python finds each match in the pattern and creates match object m for each match
# replace.get(m.group(1), m.group(1)) -> replace it if it exists in the dictionary, otherwise keep it as-is (dict.get(key, default))

for old, new in new_files.items():
    shutil.move(os.path.join(source, old), os.path.join(source, new))


