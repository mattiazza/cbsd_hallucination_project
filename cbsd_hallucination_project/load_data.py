import json
from pathlib import Path
import glob
import os
import numpy as np


def data_extraction(data_path: Path) -> dict:
    json_files = glob.glob(os.path.join(data_path, "*.json"))

    for json_file in json_files:
        # print(f"json_file # {json_files.index(json_file)}\n")

        # Load the JSON content
        with open(json_file, "r") as f:
            data = json.load(f)

        # Create my dictionary
        if json_file == json_files[0]:
            my_data = {}

        # Fill my_data dictionary
        for (
            key,
            value,
        ) in data.items():  # key: ['train', 'test'] value: list of dictionaries
            if (
                key not in my_data.keys()
            ):  # Create a dictionary for every key ('train', 'test') if the key doesn't exist already in my_data
                my_data[key] = {}
            for val in value:
                for k, v in val.items():  # k: ['input', 'output'], v: our target array
                    if (
                        k not in my_data[key].keys()
                    ):  # Create a list for every k ('input', 'output') if k doesn't exist already in the dictionary
                        my_data[key][k] = []

                    my_data[key][k].append(v)


    return my_data

def boring_data_extraction(data_path:Path) -> json:
    json_files = glob.glob(os.path.join(data_path, "*.json"))

    for json_file in json_files:
        # print(f"json_file # {json_files.index(json_file)}\n")

        # Load the JSON content
        with open(json_file, "r") as f:
            data = json.load(f)
        
        print(f"This is the {data} data\n")
        
        input("Enter to continue")



def from_num_to_col(arr: np.ndarray) -> str:
    num_to_col = {
        0: "X",  # Black
        1: "B",  # Blue
        2: "R",  # Red
        3: "V",  # Green
        4: "Y",  # Yellow
        5: "G",  # Grey
        6: "P",  # Pink
        7: "O",  # Orrange
        8: "C",  # Cyan
        9: "M",  # Brown
    }

    col_array = []
    n_row = 1

    for row in arr:
        row_str = str(n_row) + " -> " + "".join(num_to_col[i] for i in row) + "\n"
        col_array.append(row_str)
        n_row += 1

    return "".join(col_array)