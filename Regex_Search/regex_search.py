import os
import re

folder = './Regex Search'

regex = re.compile(r'Dipesh.*?\.')
result = []

for filename in os.listdir(folder):
    if filename.endswith('.txt'):
          filepath = os.path.join(folder, filename)
          with open(filepath, 'r') as file:
               content = re.split(r'(?<=[.!?])\s+',file.read())
               for sentence in content:
                    match = regex.search(sentence)
                    if match:
                         result.append(match.group())

for i in result:
     print(i)
