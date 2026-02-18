import argparse
import json
import sys

import yaml


def cli():
    # create parser with flags
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", metavar="FORMAT",
                        help="set format of output")
    return parser.parse_args()


def loading(path_to_file1, path_to_file2):
    # creates object_hook for lowering False to false and True to true
    # in json load
    def bool_hook(obj):
        new_obj = {}
        for k, v in obj.items():
            if isinstance(v, bool):
                new_obj[k] = "true" if v else "false"
            else:
                new_obj[k] = v
        return new_obj
    data1 = None
    data2 = None
    # loading data
    if path_to_file1.endswith("json"):
        with open(path_to_file1, 'r') as f:
            data1 = json.load(f, object_hook=bool_hook)

    elif path_to_file1.endswith("yaml") or path_to_file1.endswith("yml"):
        with open(path_to_file1, 'r') as f:
            data1_raw = yaml.load(f, Loader=yaml.Loader)
            data1 = bool_hook(data1_raw)
    
    if path_to_file2.endswith("json"):
        with open(path_to_file2, 'r') as f:
            data2 = json.load(f, object_hook=bool_hook)

    elif path_to_file2.endswith("yaml") or path_to_file2.endswith("yml"):
        with open(path_to_file2, 'r') as f:
            data2_raw = yaml.load(f, Loader=yaml.Loader)
            data2 = bool_hook(data2_raw)

    if not data1:
        print(f"{path_to_file1} is not found")
        sys.exit(0)
    if not data2:
        print(f"{path_to_file2} is not found")
        sys.exit(0)

    return data1, data2

    
# analyzing differences between files
def generate_diff(data1, data2):
    def items_diff(key):
        if not data2.get(key):
            return f"  - {key}: {data1[key]}\n"
        if not data1.get(key):
            return f"  + {key}: {data2[key]}\n"
        if data1[key] == data2[key]:
            return f"    {key}: {data1[key]}\n"
        return f"  - {key}: {data1[key]}\n  + {key}: {data2[key]}\n"

    all_keys = set(list(data1.keys()) + list(data2.keys()))
    all_keys = sorted(all_keys)
    result = list(map(lambda key: items_diff(key), all_keys))
    result = "".join(result)
    return "{\n" + result + "}"
