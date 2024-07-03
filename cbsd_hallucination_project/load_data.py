import numpy as np
import json
import os
import glob
from pathlib import Path
from IPython.display import clear_output


def data_extraction(
    data_path: Path, save_path: Path, llm: str, lim_print: int = 3
) -> dict:
    """
    Extract file '.json' to a dictionary from the its path
    """
    try:
        with open(save_path / f"my_data_{llm}.json", "r") as f:
            my_data = json.load(f)

        all_json_files = glob.glob(os.path.join(data_path, "*.json"))

        for n, val in enumerate(my_data["test"]):
            if llm not in val.keys():
                json_files = all_json_files[
                    n:
                ]  # Select only the files we didn't already extract

        json_files = all_json_files[n + 1 :]

    except:
        # Create my dictionary
        my_data = {"train": [], "test": []}

        # Taking all the path of our .json files
        all_json_files = glob.glob(os.path.join(data_path, "*.json"))
        json_files = all_json_files

    for json_file in json_files:
        print(
            f"json_file # {all_json_files.index(json_file)+1}/{len(all_json_files)}\n"
        )

        # Load the JSON content
        with open(json_file, "r") as f:
            data = json.load(f)

        dict_list = []

        for n, dic in enumerate(data["train"]):
            dic = number_to_colour(
                dic
            )  # Changing from numbers to letters our dictionary
            dict_list.append(dic)  # Creating the list of dictionary
            if n < lim_print:  # We decide how many training example we want to show
                print(f"input_{n+1}:\n{dic['input']}\noutput_{n+1}:\n{dic['output']}\n")

        my_data["train"].append(dict_list)  # Adding the result to our main dataset

        # Adding the 'test' part
        my_data["test"].append(number_to_colour(data["test"][0]))

        print(f"Here's the test:\n{my_data['test'][-1]['input']}")

        llm_says = input(
            "Insert here LLM's output: "  # Saving the response of the LLM
        )

        my_data["test"][-1][llm] = llm_says

        with open(save_path / f"my_data_{llm}.json", "w") as f:
            json.dump(my_data, f)

        clear_output(wait=True)  # Clear output each time

    return my_data


def number_to_letter(arr: np.ndarray) -> str:
    """
    Transform our input array in a list where each number correspond to a colour
    """
    num_to_col = {
        0: "X",  # Black
        1: "B",  # Blue
        2: "R",  # Red
        3: "V",  # Green
        4: "Y",  # Yellow
        5: "G",  # Grey
        6: "P",  # Pink
        7: "O",  # Orange
        8: "C",  # Cyan
        9: "M",  # Brown
    }

    col_array = []
    n_row = 1

    for n_row, row in enumerate(arr):
        row_str = str(n_row) + " -> " + "".join(num_to_col[i] for i in row) + "\n"
        col_array.append(row_str)

    return "".join(col_array)


def number_to_colour(my_dict: dict) -> dict:
    for k, val in my_dict.items():  # k: ['input', 'output']; val: matrices
        my_dict[k] = number_to_letter(
            val
        )  # Transform the array from number to colur (letter)

    return my_dict
