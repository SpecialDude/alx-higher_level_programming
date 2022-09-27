#!/usr/bin/python3

"""
This is script dumps all arguments to a json file

"""


import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__(
        "6-load_from_json_file"
    ).load_from_json_file


filename = "add_item.json"
args = sys.argv[1:]

e_args = load_from_json_file(filename)
args.extend(e_args)

save_to_json_file(args, filename)
