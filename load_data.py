import json
from pprint import *
from pathlib import Path

#def read_files(path):
 #   for file in path:
  #      with open('/Users/giuliabartocci/Desktop/CBSD/ARC-master/data/training.json') as f:
  #      d=json.load(f)
#        print(d)



directory = Path('/Users/giuliabartocci/Desktop/CBSD/ARC_master/data')

for file_path in directory.iterdir():
    if file_path.is_file():
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("File non trovato:", file_path)
        except PermissionError:
            print("Permesso negato per:", file_path)

