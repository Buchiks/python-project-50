import argparse
import json
import sys

def cli():
    #create parser with flags
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", metavar="FORMAT",
                        help="set format of output")
    return parser.parse_args()


def loading(args):
    #creates object_hook for changind False to false and True to true when loading  
    def bool_hook(obj):
        new_obj = {}
        for k, v in obj.items():
            if isinstance(v, bool):
                new_obj[k] = "true" if v else "false"
            else:
                new_obj[k] = v
        return new_obj
    
    #loading files
    if args.first_file.endswith("json"):
        try:
            with open(args.first_file, 'r') as f:
                data1 = json.load(f, object_hook=bool_hook)
        except FileNotFoundError:
            print(f"Файл {args.first_file} не найден")
            sys.exit(1)
    
    if args.second_file.endswith("json"):
        try:
            with open(args.second_file, 'r') as f:
                data2 = json.load(f, object_hook=bool_hook)
        except FileNotFoundError:
            print(f"Файл {args.second_file} не найден")
            sys.exit(1)
    
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
