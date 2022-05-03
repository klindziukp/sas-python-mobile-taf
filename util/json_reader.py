import json


def read_json(json_file_path):
    with open(json_file_path) as file:
        json_file = json.load(file)

    return json_file
