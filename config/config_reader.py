import os

from util import json_reader


def get_config_param(attribute):
    test_data_path = os.path.abspath("./config/config.json")
    test_data_json_file = json_reader.read_json(test_data_path)
    return test_data_json_file[attribute]
