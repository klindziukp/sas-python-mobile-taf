import os

from util import json_reader


def get_app_config_param(attribute):
    app_data_path = os.path.abspath("./config/app_config.json")
    app_data_json_file = json_reader.read_json(app_data_path)
    return app_data_json_file[attribute]


def get_device_config_param(attribute):
    device_data_path = os.path.abspath("./config/device_config.json")
    device_data_json_file = json_reader.read_json(device_data_path)
    return device_data_json_file[attribute]
