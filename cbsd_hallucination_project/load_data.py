import json
from pathlib import Path
import glob
import os


def data_extraction(data_path: Path) -> dict:
    json_files = glob.glob(os.path.join(data_path, "*.json"))
    # print(f"\njson_files: {len(json_files)}\n")

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
                    # print(
                    #     f"key: \t{key}\nk: \t{k}\nv: \t{v}\nlen(my_data[key][k]): {len(my_data[key][k])}\n"
                    # )
                    my_data[key][k].append(v)
    return my_data
